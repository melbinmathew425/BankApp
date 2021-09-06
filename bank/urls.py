from django.urls import path
from .views import AccountCreateView,SigninView,BalanceView,FundTransferView,PaymentHistoryView,SignOutView,TransactionFilterView,IndexView,Home
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path("home",Home,name="home"),
    path("login",SigninView.as_view(),name="signin"),
    path("logout",SignOutView.as_view(),name="signout"),
    path("create",AccountCreateView.as_view(),name="create"),
    path("balance", BalanceView.as_view(),name="balance"),
    path("transfer",FundTransferView.as_view(),name="transfer"),
    path("history",PaymentHistoryView.as_view(),name="history"),
    path("filter",TransactionFilterView.as_view(),name="filter"),
    path("index",IndexView,name="index")
]
