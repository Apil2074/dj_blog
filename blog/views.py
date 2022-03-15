from django.shortcuts import render
from django.http import HttpResponse
# from matplotlib.pyplot import title
from blog.models import Post

# Create your views here.


def hello(request):  
    allpost= Post.objects.all()[:3]
    # print(allpost.title)
    context={'allpost':allpost}
    return render(request, 'index.html' , context)  
    