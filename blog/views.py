from django.shortcuts import render


posts = [
    {
        'author': 'Author 1',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
{
        'author': 'Author 2',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 27, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

