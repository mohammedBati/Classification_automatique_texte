from django.conf.urls import url
from . import views


app_name='Post'
urlpatterns = [
          #url(r'^$',views.all_posts ,name='all_posts'),
          #url(r'^(?P<id>\d+)$',views.post ,name='post'),
         # url(r'^external' , views.external),
          url(r'^$', views.home ,name='home'),
          url('index/', views.calassifier ,name='index'),
          #url('index/', views.upload_multiple_files ,name='index'),
          url(r'register/', views.registerPage, name="register"),
          url(r'login/', views.loginPage, name="login"),
          url('logout/', views.logoutUser, name="logout"),
          #url('tx/', views.upload_multiple_files ,name='index'),
]
