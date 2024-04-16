from django import forms  
from employee.models import Employee  
class EmployeeForm(forms.ModelForm):
    file = forms.FileField()  
    class Meta:  
        model = Employee  
        fields = "__all__"