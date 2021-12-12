from django.urls import path
from .views import CountryList, CountryDetail

urlpatterns = [
    path('', CountryList.as_view(), name = 'country_list'),
    path('<int:pk>/',CountryDetail.as_view(), name = 'country_detail')

]