"""config URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from Authentication import views as auth_view
from Account import views as act_view
from Photo import views as p_view
from Comment import views as c_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', act_view.LoggedInView.as_view(), name='homepage'),
    # path('', auth_view.index_view, name='homepage'),
    path('signup/', auth_view.SignupView.as_view()),
    path('login/', auth_view.LoginView.as_view()),
    path('logout/', auth_view.LogoutView.as_view()),
    # path('welcome/', act_view.LoggedInView.as_view(), name='logged'),
    path('post/', p_view.PostImage.as_view()),
    path('post/<int:post_id>/', p_view.PostDetail.as_view()),
    # path('comment/<int:post_id>/', p_view.PostComment.as_view()),
    path('delete/<int:post_id>/', p_view.PostDelete.as_view()),
    path('profile/<int:id>/', act_view.profile_detail),
    path('edit/<int:id>/', act_view.edit),
    # path('like/<int:post_id>/', p_view.like_unlike),
    path('like/<int:post_id>/', p_view.like_photo),
    path('unlike/<int:post_id>/', p_view.unlike_photo)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
