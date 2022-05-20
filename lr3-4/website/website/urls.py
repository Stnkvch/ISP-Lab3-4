
"""URL project configuration"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews
from authorization import views as userViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sign_in', authViews.LoginView.as_view(template_name='authorization/sign_in.html'), name='auth_page'),
    path('exit/', authViews.LogoutView.as_view(template_name='main/product.html'), name="exit"),
    path('sign_up', userViews.register, name='regis_page'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)