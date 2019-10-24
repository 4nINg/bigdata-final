from django.conf.urls import url
from api.views import auth_views, data_views

urlpatterns = [
    url('auth/signup/$', auth_views.signup, name='sign_up'),
    url('auth/login/$', auth_views.login, name='login'),
    url('auth/session/$', auth_views.session, name='session'),
    url('auth/logout/$', auth_views.logout, name='logout'),
    url('fnc/$', data_views.create_fnc_data, name='create_fnc_data'),
]
