from django.shortcuts import render , render_to_response, redirect
from .models import rating

# Create your views here.
def home (request):
    return render(request, 'html/home.html',{'rating': rating.objects.get(name='home')})

def addlike(request):
    rat = rating.objects.get(name='home')
    rat.like = rat.like + 1
    rat.save()
    return redirect('/#vote')

def adddislike(request):
    rat = rating.objects.get(name='home')
    rat.dislike = rat.dislike+1
    rat.save()
    return redirect('/#vote')
