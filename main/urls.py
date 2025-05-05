from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# urls.py

# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('playlist/', views.playlist_user, name='playlist'),
    # Add this if you want category-based views too:
    path('playlist/<str:category>/', views.playlist_category_view, name='playlist_category'),
]


urlpatterns = [
    path("", views.default, name='default'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_auth, name="login_auth"),  
    path("logout/", views.logout_auth, name="logout_auth"),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page') 
     
]