from django.conf.urls import url

from . import views
from . import welcome
from . import stu

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^welcome/',welcome.welcome,name='welcome'),
    url(r'^login/',welcome.login,name='welcome_login'),
    url(r'^signup/',welcome.signup,name='welcome_signup'),
    url(r'^homepage/',welcome.homepage,name='homepage'),
    url(r'^stu_search/',stu.stu_search,name='stu_search'),
    url(r'^stu_res_search/',stu.stu_res_search,name='stu_res_search'),
    url(r'^stu_tutor_info/(.+)/',stu.stu_tutor_info,name='stu_tutor_info'),
    url(r'^stu_book_confirm/(?P<session_id>[0-9]+)/',stu.book_confirm,name='book_confirm'),
    url(r'^stu_book_success/(?P<session_id>[0-9]+)/',stu.book_success,name='book_success'),
    url(r'^stu_view_book_session/',stu.view_book_session,name='view_book_session'),
    url(r'^stu_cancel_confirm/(?P<session_id>[0-9]+)/',stu.cancel_confirm,name='cancel_confirm'),
    url(r'^stu_cancel_success/(?P<session_id>[0-9]+)/',stu.cancel_success,name='cancel_success'),

]