from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cat-list/<cat_id>',views.cat_list,name='cat-list'),
    path('news-details/<slug>',views.news_details,name='news-details'),
    path('news-search',views.news_search,name='news-search')
]
