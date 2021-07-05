from django.urls import path
from . import views

app_name = 'first'

urlpatterns = [
    path('', views.Home.as_view(), name ='home'),
	path('create/', views.TodoCreate.as_view(), name='create_todo'),
    path('<slug:myslug>/', views.DetailTodo.as_view(), name = 'detail_todo'),
    path('delete/<int:pk>/' , views.DeleteTodo.as_view(), name = 'delete_todo'),
    path('update/<int:pk>/', views.UpdateTodo.as_view(), name = 'update_todo'),
    path('<int:year>/<str:month>/', views.MonthTodo.as_view(), name ='month_todo'),
]