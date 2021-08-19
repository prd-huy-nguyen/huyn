from django import forms
from polls.models import Customer, TypeCustomer, Employee


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'age', 'address', 'gender', 'typeCustomer')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'age' : forms.NumberInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
            'gender' : forms.CheckboxInput(attrs={'class': '', "style":"display: block"}),
            'typeCustomer' : forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Tên',
            'age' : 'Tuổi',
            'address': 'Địa chỉ',
            'gender' : 'Giới tính(tích vào nếu là nam)',
            'typeCustomer': 'Loại khách hàng'
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'age', 'address', 'gender', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.CheckboxInput(attrs={'class': '', "style": "display: block"}),
            'image': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Tên',
            'age': 'Tuổi',
            'address': 'Địa chỉ',
            'gender': 'Giới tính(tích vào nếu là nam)',
            'image': 'Hình ảnh'
        }

