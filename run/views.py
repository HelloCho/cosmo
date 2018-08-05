from django.shortcuts import render, redirect
from django.http import HttpResponse

# My Need Class
from run.models import ProductModel, Product
from django.db.models import F, Sum
from run.form import PostForm

# LoginForm
from .form import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

# Create your views here.
def index(request):
    createdResult = Product.objects.filter(isDisposal=False).values('product_id', 'isDisposal').annotate(name=F('product__name'),code=F('product__code'),total=Sum('quantity'))
    disposalResult = Product.objects.filter(isDisposal=True).values('product_id', 'isDisposal').annotate(name=F('product__name'),code=F('product__code'),total=Sum('quantity'))
    return render(request, "run/index.html", {"createdResult":createdResult, "disposalResult":disposalResult})

def detail(request, itemKey, disposalFlag):
    if (disposalFlag == 'False'):
        result = Product.objects.filter(product_id=itemKey, isDisposal='False').values('madeYear', 'isDisposal').annotate(name=F('product__name'), quantity=Sum('quantity')).order_by('-madeYear')
    else:
        result = Product.objects.filter(product_id=itemKey, isDisposal='True').values('madeYear', 'isDisposal').annotate(name=F('product__name'), quantity=Sum('quantity')).order_by('-madeYear')

    return render(request, "run/detail.html", {"result":result})

def post(request):
    if request.method == 'POST':
        # Post 일 경우
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # Get 일 경우
        form = PostForm()
        return render(request, "run/form.html", {"form":form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'run/login.html', {'form': form})
