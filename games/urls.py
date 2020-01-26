from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('<int:game_id>/results/', views.results, name='results'),
    path('<int:game_id>/score/', views.score, name='score')
]
