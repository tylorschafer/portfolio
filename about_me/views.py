from django.shortcuts import render

def about_me_index(request):
    return render(request, 'about_me.html')
