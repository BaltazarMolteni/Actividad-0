from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Encuesta


def index(request):
    latest_question_list = Encuesta.objects.order_by("-fecha_publ")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "encuestas/index.html", context)

def detalle(request, question_id):
    question = get_object_or_404(Encuesta, pk=question_id)
    return render(request, "encuestas/detalle.html", {"encuesta": question})

def resultados(request, question_id):
    response = "Estás viendo las respuestas a la pregunta %s."
    return HttpResponse(response % question_id)


def voto(request, question_id):
    return HttpResponse("Estás votando en la pregunta %s." % question_id)