from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
#    return HttpResponse('this is my home page')
    return render(request, 'home.html')

def about(request):
#    return HttpResponse('this is my about page')
    return render(request, 'about.html')
def projects(request):
#    return HttpResponse('this is my projects page')
    return render(request, 'projects.html')
def contact(request):
  #  return HttpResponse('this is my contact page')
    return render(request, 'contact.html')
def Thanks(request):
 #   return HttpResponse('This is my Thank you notes page')
    return render(request, 'Thanks.html')

def articles(request):
    return render(request, 'articles.html')

