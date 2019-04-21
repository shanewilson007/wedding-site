from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', login, {'template_name':'home/welcome.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^home/comments/$', views.PostView.as_view(), name='comments'),
    url(r'^home/rsvp/$', views.ReceptionView.as_view(), name='reception'),
    # url(r'^register/$', views.register, name='register'),
]
