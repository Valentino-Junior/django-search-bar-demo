from django.shortcuts import render
from .models import Post
from django.db.models import Q 
# Create your views here.
def welcome(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post))

    else:
    # If not searched, return default posts
    # posts = Post.objects.all()
        posts = Post.objects.all().order_by('-date_created')

    # if request.method == 'POST':
    #     new_img =Post(
    #      science_image = request.FILES['pic']   
    #     )
    #     new_img.save()

    return render (request,'home.html', {'posts':posts},)

# Create your views here.
def nav(request):
    return render (request,'navbar.html' )

def base(request):
    return render (request,'base.html' )
