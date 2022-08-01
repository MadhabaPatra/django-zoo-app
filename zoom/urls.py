from django.urls import path

from . import views

urlpatterns = [

    # path: /
    path('', views.index, name='index'),

    # path: /callback
    path('callback', views.HandleCallback, name='callback'),

    # path: /dashboard
    path('dashboard', views.Dashboard, name='dashboard'),

    # path: /meeting
    path('meeting', views.Meeting, name='meeting'),

    # path: /error
    path('error', views.error, name='error'),
]