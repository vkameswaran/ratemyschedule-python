from django.shortcuts import render
from .utils.grades import findInfo

# Create your views here.

def index(request):
    context = {
        "courses": "",
    }
    if ("courses" in request.GET and request.GET["courses"]):
        # TODO: Check if I need to clean this input
        returnText = findInfo(request.GET["courses"])
        context["info"] = returnText
        context["courses"] = request.GET["courses"]
    return render(request, 'ratings/index.html', context=context)
