from django.conf.urls import url,include
from . import views

app_name="blogs"

urlpatterns=[
	url(r'^$',include('home.urls')),
	url(r'^blogs/$',views.blogs_show_all,name='show_all'),
	url(r'^blogs/(?P<blog_id>[0-9]+)/$',views.blog_details,name='details'),
	url(r'^bloggers/$',views.all_bloggers,name='all_bloggers'),
	url(r'^bloggers/(?P<author_id>[0-9]+)/$',views.blogger_detail,name='blogger_details'),
	url(r'^blogs/(?P<blog_id>[0-9]+)/create/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^blogger/$',views.register_blogger,name='register_blogger'),
	url(r'^blogs/add_post$',views.add_post,name='add_post'),
]