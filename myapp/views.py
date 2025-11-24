from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Sadə statik veb səhifəsini göstərən view funksiyası.
    HTML şablonunu render edərək istifadəçiyə göstərir.
    """
    return render(request, 'myapp/index.html')
