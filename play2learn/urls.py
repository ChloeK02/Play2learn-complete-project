
from django.contrib import admin
from django.urls import path, include
from games import views

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),
    path('accounts/', include('allauth.urls')),
    path("admin/", admin.site.urls),
    path('', include("games.urls")),
]
