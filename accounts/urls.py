from django.conf.urls import url
from . import views as accoutns_views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', accoutns_views.signup, name = 'signup'),
    url(r'^login/', accoutns_views.usrlogin, name = 'login'),
    url(r'^logout/', accoutns_views.usrlogout, name = 'logout'),
]
