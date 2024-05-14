"""
URL configuration for courrier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from Dashboard.views import *
from accounts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('index/', IndexView.as_view(), name="index"),
    path('courrier/add', AddCourrierView.as_view(), name='add_courrier'),
    path('courrier/<int:pk>/', CourrierDetailView.as_view(), name='courrier_detail'),
    path('rappel/create/<int:courrier_id>', CreateRappelView.as_view(), name='create_rappel'),
    path('rappel/update/<int:pk>/', UpdateRappelView.as_view(), name='update_rappel'),
    path('rappel/delete/<int:rappel_id>/', delete_rappel, name='delete_rappel'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
