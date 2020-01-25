from django.shortcuts import render
from .models import Post

  
# posts = [
#   {
#     'author': 'User_01',
#     'title': 'this is tile one',
#     'content': 'loremsaf sad fsad fsad f sd ',
#     'date_posted': 'August 27, 2018'
#   },
#   {
#     'author': 'User_02',
#     'title': 'this is tile Two',
#     'content': 'loremsaf sad faef aessad fsad f sd ',
#     'date_posted': 'August 28, 2018'
#   }
# ]

def home(request):
  posts = Post.objects.all()
  context = {
    'title': 'Home',
    'posts': posts,
  }
  return render(request, 'blog/home.html', context)


def about(request):
  return render(request, 'blog/about.html')