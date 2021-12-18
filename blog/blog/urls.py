from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=TemplateView.as_view(template_name='posts/index.html'),
        name='index'
    ),
    path(
        route='post/my-post.html',
        view=TemplateView.as_view(template_name='posts/detail.html'),
        name='detail'
    ),
    path(
        route='sobre-mi',
        view=TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    path('', include(('users.urls', 'users'), namespace='users')),
]