from django.conf.urls import url
from . import views
#####
urlpatterns = [
    url(r'^$',views.BlogListView.as_view(),name='blogs'),
    url(r'^(?P<pk>\d+)$',views.BlogDetailView.as_view(),name='blog-detail'),
    url(r'^authors/',views.AuthorListView.as_view(),name='authors'),
    url(r'^author/(?P<pk>\d+)$',views.AuthorDetailView.as_view(),name='author-detail'),
    url(r'^(?P<pk>\d+)/comment/$',views.BlogCommentCreate.as_view(),name='blog-comment'),
]
