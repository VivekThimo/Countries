from django.shortcuts import render

# Create your views here.
def kindle(request):
    return render(request, 'Europe/index.html')