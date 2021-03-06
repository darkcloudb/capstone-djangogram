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
from Video import views as v_view
from config import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', act_view.LoggedInView.as_view(), name='homepage'),
    path('signup/', auth_view.SignupView.as_view()),
    path('login/', auth_view.LoginView.as_view()),
    path('logout/', auth_view.LogoutView.as_view()),
    path('post/', p_view.PostImage.as_view()),
    path('post/<int:post_id>/', p_view.PostDetail.as_view()),
    path('delete/<int:post_id>/', p_view.PostDelete.as_view()),
    path('uncomment/<int:post_id>/', p_view.CommentDelete.as_view()),
    path('superdel/<int:post_id>/', p_view.SuperDelete.as_view()),
    path('profile/<int:id>/', act_view.profile_detail, name='profile'),
    path('edit/<int:id>/', act_view.EditProfile.as_view()),
    path('like/<int:post_id>/', p_view.like_photo),
    path('unlike/<int:post_id>/', p_view.unlike_photo),
    path('video/', v_view.play_vid),
    path('video_page/', act_view.vid_page, name='video'),
    path('viddelete/<int:post_id>/', v_view.VidDelete.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "config.views.page_not_found_view"

# handler500 = "config.views.nice_job_view"

handler403 = "config.views.forbidden_view"
