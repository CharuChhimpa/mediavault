"""
URL patterns for 'web' app
"""
from django.conf.urls import url
from django.conf.urls.static import static

from mediavault import settings
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/?', views.login, name='explore'),
    url(r'^shared-items/?$', views.shared_items, name='shared-items'),
    url(r'^shared-items/(?P<id>[0-9]+)/?$', views.single_shared_item,
        name='single-shared-item'),
    url(r'^media/?$', views.media, name='media'),
    url(r'^media/(?P<id>[0-9]+)/?$', views.media_page, name='media-page'),
    url(r'^media-get/(?P<id>[0-9]+)/?$', views.media_get, name='media-get'),
    url(r'^explore/?$', views.explore_root, name='explore-root'),
    url(r'^explore/(?P<id>[0-9]+)/?$', views.explore, name='explore'),
    url(r'^master/user/?$', views.master_user, name='master-user'),
    url(r'^master/user/add/?$', views.master_user_add, name='master-user-add'),
    url(r'^master/user/modify/?$', views.master_user_modify,
        name='master-user-modify'),
    url(r'^suggestions/?', views.show_suggestions, name='show_suggestions'),
    url(r'^logout/?', views.logout, name='logout'),
    url(r'^online/?$', views.online, name='online'),
    url(r'^online/(?P<id>.*)/?$', views.online_single, name='online_single'),
    url(r'^change-password/?', views.change_password, name='change_password'),
    url(r'^master/user/reset/?$', views.reset_password, name='reset-password'),
    url(r'^test', view=views.test, name='test'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
