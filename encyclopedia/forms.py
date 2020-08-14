from django import forms

class newContent(forms.Form):
    title = forms.CharField(label = "Insert title here", max_length= 100)
    content = forms.CharField(label="write the content here",max_length=1000)