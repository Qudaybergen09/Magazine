from django.shortcuts import render
from .models import Post
from .models import Comment
from .forms import CommentForm
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def HomePage(request):
    return render(request, 'post/index.html')

def aboutPage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/about.html', context) 

def profilesPage(request):
    return render(request, 'post/profiles.html')

def aboutdetail(request, pk):
    post = get_object_or_404(Post,id=pk)
    comments = Comment.objects.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'post': post
    }
    return render(request, 'post/aboutdetail.html', context)


"""def newPostPage(request):
    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():    
            form.save()
            return HttpResponseRedirect(redirect_to='/post/')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request=request, template_name='post/new_post.html', context=context)
"""

def buyPage(request):
    return render(request, 'post/buy.html')

def profile1Page(request):
    return render(request, 'post/profile1.html')

def profile2Page(request):
    return render(request, 'post/profile2.html')


def newPostPage(request):

    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():    
            form.save()
            return HttpResponseRedirect(redirect_to='/about/')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request=request, template_name='post/newpost.html', context=context)