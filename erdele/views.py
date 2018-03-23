from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "erdele/index.html", context=context)


def signin(request):
    return render(request, 'erdele/login.html')

def signup(request):
    return render(request, 'erdele/register.html')
