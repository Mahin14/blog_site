from django.urls import path
from App_Blog import views
app_name='App_Blog'
urlpatterns = [
    path('blog/',views.BlogList.as_view(),name='blog_list'),
    path('write',views.CreateBlog.as_view(),name='create_blog'),
   path('details/<slug:slug>',views.blog_details,name='blog_details'),
   path('like/<pk>/',views.liked,name='like_post'),
   path('unlike/<pk>/',views.unliked,name='unlike_post'), 
   path('my-blog',views.MyBlogs.as_view(),name='my_blogs'), 
   path('edit-blog/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'), 
   path('delete-blog/<pk>/',views.DeleteBlog.as_view(),name='delete_blog'), 

    


]
