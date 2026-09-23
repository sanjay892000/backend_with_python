from django.shortcuts import render
# Create your views here.

def notes(request):
    return render(request, "notes/notes.html")

def createnotes(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        tag = request.POST.get("tag", "").strip()
    
    render()