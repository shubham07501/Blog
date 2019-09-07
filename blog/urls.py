"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from  django.contrib.auth.views import LoginView
from  blogs import views
from  django.contrib.auth import login as auth_login
from  django.contrib.auth import logout as auth_logout



from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include("home.urls")),
    url(r'^blog/',include("blogs.urls")),
    url(r'^login/$',LoginView.as_view(template_name='blogs/login.html'),name='login'),
    url(r'^logout/$',views.log_me_out,name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
