from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from markdown2 import Markdown
from django.urls import reverse
import random
from django.contrib import messages
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def randomPage(request):
    entries = util.list_entries()
    title = random.choice(entries)
    page =  util.get_entry(f"{title}")
    markdown = Markdown()
    contenido = markdown.convert(page)     
    return render(request, "encyclopedia/entryPage.html" ,{
        "contenido" : contenido,
        "title" : title
    })

  
def entryPage(request, title):
    try:
        page =  util.get_entry(f"{title}")
        print(page)
        markdown = Markdown()

        contenido = markdown.convert(page)  

        print("todo bien ? ")
        return render(request, "encyclopedia/entryPage.html" ,{
            "contenido" : contenido,
            "title" : title
        })
    except:        
        return render(request, "encyclopedia/notFound.html" ,{
            "title" : title
        })


def createNewPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        title = request.POST['title']   
        content = request.POST['content'] 
        if util.get_entry(f"{title}"):
            messages.error(request, "the content saved already exist")
            return render(request, "encyclopedia/createNewPage.html")        
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entryPage', args=(title,)))
        # check whether it's valid:
        
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "encyclopedia/createNewPage.html")



def searchPage(request):
    search = request.GET.get('q')  
    list_entries = util.list_entries()      
    if search in list_entries: 
        page =  util.get_entry(search)  
        markdown = Markdown()
        contenido = markdown.convert(page)         
        return render(request, "encyclopedia/entryPage.html" ,{
            "contenido" : contenido,
            "title" : search
        })
    elif [match for match in list_entries if search in match]:
        matches= [match for match in list_entries if search in match]   
        return render(request, "encyclopedia/searchPage.html", {
            "matches": matches
        })

 



def editPage(request, title):
    print("esta en editar")

    if request.method == 'POST':
        title = request.POST['title']   
        content = request.POST['content'] 

        util.save_entry(title ,content)
        print("editando pagina wtfs")

        return HttpResponseRedirect(reverse('entryPage', args=(title,)))     
        # check whether it's valid:
        
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # if a GET (or any other method) we'll create a blank form
    else:
        page =  util.get_entry(f"{title}")
        print("y se fue por acá ")
           
        return render(request, "encyclopedia/editPage.html" ,{
            "contenido" : page,
            "title" : title
        })    
  






