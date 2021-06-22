from django.urls import path
from .views import TableList, TableDetail
from django.contrib import admin

urlpatterns = [
    path('table/', TableList.as_view(), name="table_list"),
    path('table/<int:pk>/', TableDetail.as_view()),

]

admin.site.site_header = 'Denver Scorpions'
admin.site.site_title = 'Denver Scorpions'
