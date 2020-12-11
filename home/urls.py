from django.contrib import admin
from django.urls import path
from . import views
from . import models


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.head,name="homepage"),
    path('logout',views.logout,name="logout"),

    
]
