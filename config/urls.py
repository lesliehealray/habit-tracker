"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from django.views.generic.base import TemplateView
from tracker.views import SignUpView
from rest_framework.urlpatterns import format_suffix_patterns
from tracker import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', include('django.contrib.auth.urls')),
    path('create_habit/', views.create_habit, name='create_habit'),
    path('habit/<slug:slug>', views.habit_detail, name='habit_detail'),
    path('api/log/<int:pk>/', views.logapi.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
    SHOW_TOOLBAR_CALLBACK = True
