from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView,TemplateView,View
from App_Blog.models import Blog,Comment,likes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #for class base views
from django.urls import reverse,reverse_lazy
from App_Blog.forms import CommentForm
import uuid




# def blog_list(request):
#     return render(request,'App_Blog/blog_list.html',context={})


class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name='App_Blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')
    


    def form_valid(self,form):
        # blog_obj1 =form()
        
        user=self.request.user

        if not user.is_authenticated:
            return HttpResponseRedirect(reverse("App_login:login"))
        else:
            blog_obj =form.save(commit=False)
            blog_obj.author = self.request.user
            title = blog_obj.blog_title
            blog_obj.slug = title.replace('','-')+'-'+ str(uuid.uuid4())
            blog_obj.save()
            return HttpResponseRedirect(reverse("index"))



class BlogList(ListView):
    context_object_name ='blogs'
    model = Blog
    template_name='App_Blog/blog_list.html'
    # queryset=Blog.objects.order_by("-publish_date")



# @login_required
def blog_details(request,slug):
    blog=Blog.objects.get(slug=slug)
    comment_form=CommentForm()
    liked=0
    if  request.user.is_authenticated:
        already_liked=likes.objects.filter(blog=blog,user=request.user)
        if already_liked:
            liked=True
        else:
            liked=False
    
    if request.method =="POST":    
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("App_login:login"))
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment_obj=comment_form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.blog = blog
            comment_obj.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':slug}))
    return render(request,'App_Blog/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})



class MyBlogs(LoginRequiredMixin,TemplateView):
    template_name = 'App_Blog/my_blogs.html'

class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields=('blog_title','blog_content','blog_image')
    template_name='App_Blog/edit_blog.html'
    def get_success_url(self,**kwargs):
        return reverse_lazy('App_Blog:blog_details',kwargs={'slug':self.objects.slug})


class DeleteBlog(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name='App_Blog/delete_blog.html'
    success_url =reverse_lazy('App_Blog:my_blogs')



@login_required
def liked(request,pk):
    blog =Blog.objects.get(pk=pk)
    user=request.user
    already_liked=likes.objects.filter(blog=blog,user=user)
    if not already_liked:
        liked_post=likes(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':blog.slug}))



@login_required
def unliked(request,pk):
    blog =Blog.objects.get(pk=pk)
    user=request.user
    already_liked=likes.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':blog.slug}))

