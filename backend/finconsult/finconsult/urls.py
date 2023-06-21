"""finconsult URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

from django.urls import path, re_path

from django.utils.deprecation import MiddlewareMixin


urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('', views.index, name='home'),
    path('notes/<int:id>/', views.notes, name='notes'),
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the new meeting view
    path('newmeeting/', views.newmeeting, name='newmeeting'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    # add a url for the notes view
    path('notes/<int:id>/', views.notes, name='notes'),
    # add a url for the calendar view
    path('calendar/<str:username>/', views.calendar, name='calendar'),
    path('newMeeting/', views.newmeeting, name='newmeeting'),
    re_path(r'^.*\.*', views.pages, name='pages'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
