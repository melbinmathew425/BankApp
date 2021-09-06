from django import forms
from django.contrib.auth.forms import UserCreationForm
from bank.models import MyUser
# from .views import *

class GetUserAccountMixin():
    def get_user_account(self,acc_no):
        try:
            return MyUser.objects.get(account_number=acc_no)
        except:
            return None

class AccountCreationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["first_name","username","email","password1","password2",
                "account_number","account_type","phone","balance"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class TransactionForm(forms.Form,GetUserAccountMixin):
    from_account_number=forms.CharField(max_length=16,widget=forms.TextInput(attrs={"class": "form-control"}))
    to_account_number=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_account_number=forms.CharField(max_length=16,widget=forms.TextInput(attrs={"class": "form-control"}))
    amount=forms.FloatField(widget=forms.TextInput(attrs={"class": "form-control"}))
    notes=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        from_account_number=cleaned_data.get("from_account_number")
        to_account_number=cleaned_data.get("to_account_number")
        confirm_account_number=cleaned_data.get("confirm_account_number")
        amount=cleaned_data.get("amount")
        if to_account_number !=confirm_account_number:
            msg="account number mismatch"
            self.add_error(confirm_account_number,msg)
        user=GetUserAccountMixin()
        account=user.get_user_account(confirm_account_number)
        if not account:
            msg="invalied account number"
            self.add_error("confirm_account_number",msg)
        account=user.get_user_account(from_account_number)
        if account.balance<amount:
            msg="insufficient amound"
            self.add_error("amount",msg)

