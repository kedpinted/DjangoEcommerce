from django.urls import path
from.import views

urlpatterns = [
    # path('', views.index='index')
    path('', views.index, name="index")
]
