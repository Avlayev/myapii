from django.urls import path
from .views import IncomeList, IncomeDetail

urlpatterns = [
    path('', IncomeList.as_view(), name='income'),
    path('', IncomeDetail.as_view(), name='income-detail'),

]