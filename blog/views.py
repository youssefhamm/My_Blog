from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')

def blog_view(request):
    return render(request, 'blog.html')

def features_view(request):
    return render(request, 'features.html')

def about_view(request):
    return render(request, 'about.html')

#def contact_view(request):
#    return render(request, 'contact.html')