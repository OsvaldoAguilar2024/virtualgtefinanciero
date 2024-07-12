
from django.urls import path , include
from django.conf.urls.static import static
from. import views
from django.conf import settings
from appchatbot import views
from django.contrib import admin


urlpatterns = [
    path('super/', admin.site.urls),
    path('', views.index, name='index'),
    path('account/', include('users_app.urls')),
  
]
