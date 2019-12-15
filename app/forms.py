from django import forms

class TestForm(forms.Form):
    name = forms.CharField(label = "名前")
    age = forms.IntegerField(label = "年齢")
    hometown = forms.CharField(label = "出身")
    hobey = forms.CharField(label= '趣味')