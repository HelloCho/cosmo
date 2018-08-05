from django import forms
from run.models import Product, ProductModel
import datetime

# login
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        year = datetime.date.today().year
        model = Product
        fields = ('product', 'madeYear', 'quantity', 'isDisposal',)
        widgets = {
            'product':forms.Select(attrs={'class':'form-control'}),
            'madeYear': forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'isDisposal': forms.CheckboxInput(),
        }
        labels = {
            'product': "모델 명",
            'madeYear': "생산년도",
            'quantity': "수량",
            'isDisposal': "폐기 여부",
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password'] # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
