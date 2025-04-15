from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola Mundo. Esta es la página de inicio de la aplicación encuestas.")