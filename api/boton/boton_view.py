from django.shortcuts import render

# Create your views here.

def boton_view(request):
    
    template_view = "ui-buttons.html"
    
    return render(request,template_name=template_view)