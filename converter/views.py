from django.shortcuts import render , HttpResponse
from .forms import EditorForm
# Create your views here.



def home(request):
    if request.method == "POST":
        return HttpResponse("Post Method ON!")


    title = 'خانه'
    form = EditorForm
    context = {
        'title' : title,
        'form' : form
    }
    return render(request , 'converter/home.html' , context)