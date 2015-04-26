from django.conf.urls import include, url
from django.contrib import admin

from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'osu_courses_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^majors/$', views.majors, name='majors'),
    url(r'^classes/$', views.classes, name='classes'),
    url(r'^class_details/$', views.class_details, name='class_details'),
]
