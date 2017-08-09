from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.project_list, name='project_list'),
    url(r'^project/$', views.project_list, name='project'),
    url(r'^project/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
    url(r'^project/(?P<pk>\d+)/model/$',  views.model_list, name='model_list'),
    url(r'^project/(?P<pk>\d+)/model/new/$', views.new_model, name='new_model'),
    url(r'^project/(?P<pk>\d+)/edit/$', views.project_list, name='project_edit'),
    url(r'^project/new/$', views.new_project, name='new_project'),
    url(r'^model/(?P<pk>\d+)/$',  views.model_detail, name='model_detail'),
    url(r'^model/(?P<pk>\d+)/edit/$', views.project_list, name='model_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
