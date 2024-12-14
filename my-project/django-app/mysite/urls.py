from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views  # Blog uygulamasının görünümlerini içe aktarın

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Blog uygulamasının URL'lerini dahil edin
    path('', blog_views.index, name='home'),  # Ana sayfa için blog uygulamasının index görünümünü kullanın
]