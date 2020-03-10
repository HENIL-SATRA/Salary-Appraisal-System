from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signupform/', views.signupform, name='signupform'),
    path('', views.welcome, name='welcome'),
    path('selectType/', views.selectType, name="selectType"),
    path('signinhr/', views.signinhr, name="signinhr"),
    path('signinemp/', views.signinemp, name="signinemp"),
    path('signinit/', views.signinit, name="signinit"),
    path('profile/<int:sn>', views.profile, name="profile"),
    path('profileform/', views.profileform, name="profileform"),
    path('hr/', views.hr, name="hr"),
    path('emp/', views.emp, name="emp"),
    path('it/', views.it, name="it"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)