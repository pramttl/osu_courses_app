from django.conf.urls import include, url
from django.contrib import admin

from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'osu_courses_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^majors$', views.majors, name='majors'),
    url(r'^courses$', views.majors, name='coures'),
    url(r'^course_details$', views.course_details, name='course_details'),
]
