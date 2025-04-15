from django.http import HttpResponse
from .models import Encuesta

def index(request):
    latest_question_list = Encuesta.objects.order_by("-fecha_publ")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detalle(request, question_id):
    return HttpResponse("Estás viendo la pregunta %s." % question_id)


def resultados(request, question_id):
    response = "Estás viendo las respuestas a la pregunta %s."
    return HttpResponse(response % question_id)


def voto(request, question_id):
    return HttpResponse("Estás votando en la pregunta %s." % question_id)