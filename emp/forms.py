from django import forms
from .models import Emp


class FeedbackForm(forms.Form):
    name  = forms.CharField(label="name",max_length=100)
    phone = forms.CharField(label="phone", max_length=10)
    email = forms.EmailField(label="email",max_length=100)
    feedback = forms.CharField(label="feedback",max_length=200, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ["name","emp_id","address","phone"]

