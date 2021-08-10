"""correos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from enviomail.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='home'),

    #ENVIAR EMAIL
    path('EnviarMailAuto/',EnviarMailAuto, name ='EnviarMailAuto'),
    # path('Mail_list/',Mail_list, name ='Mail_list'),
    path('report_SendMail_excel/',Reporte_SendMail_excel.as_view(), name ='report_SendMail_excel')
]
