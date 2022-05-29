from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # comma 제발 붙입시다.
    path('<int:question_id>/', views.detail),
]