from django.urls import path
from . import views


urlpatterns = [
    # path('', views.HomePageView.as_view(), name="home"),
    path('', views.home, name="home"),
    path('news-list/', views.newslistview, name="news_list"),
    path('news-sport/', views.SportNewsView.as_view(), name="sport"),
    path('news-since/', views.SinceNewsView.as_view(), name="ilmiy"),
    path('news-cultural/', views.CulturalNewsView.as_view(), name="madaniy"),
    path('news-foreign/', views.ForeignNewsView.as_view(), name="xorij"),
    path('news-single/<slug:news>/', views.newsdetailview, name="news_detail"),
    path('news-search/', views.newssearchview, name="news_search"),
    path('our-contact/', views.contactview, name="contact"),
]