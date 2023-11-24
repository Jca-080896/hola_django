from django.http import HttpResponse
 
def index(request):
    return HttpResponse('Hola Mundo. Como estas? <br><br>Yair Escaamilla </a>')
