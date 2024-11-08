"""
URL configuration for django_project_ospelnikov project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from project_first_app import views
from project_first_app.views import CarList, owner_form, CarForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:owner_id>', views.owner),
    path('list_owners/', views.list_owners),
    path('list_cars/', CarList.as_view()),
    path('owner_form/', owner_form),
    path('car_form/', CarForm.as_view(success_url="/car_form/")),

]

