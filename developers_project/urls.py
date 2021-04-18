from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include("home.urls")), 
    path('', include('django.contrib.auth.urls')),
    path('developers/', include("developers.urls")),
    path('admin/', admin.site.urls),    
    # path('', auth_views.LoginView.as_view()),
    # path('', auth_views.LoginView.as_view(template_name='login.html')),
    
]
