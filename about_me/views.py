from django.shortcuts import render
from about_me.models import AboutMe

def about_me_index(request):
    about_me = AboutMe.objects.all()
    context = {
        'about_me': about_me,
    }
    return render(request, 'about_me.html', context)
