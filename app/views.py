from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,'sample.html')
def sample1(request):
    return render(request,'sample1.html')