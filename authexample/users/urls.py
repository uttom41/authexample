from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='user_index'),
    #  path('signup/', views.SingUp.as_view())
]
