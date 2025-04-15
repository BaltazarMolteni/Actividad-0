from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Encuesta, Respuesta
from django.urls import reverse

def index(request):
    latest_question_list = Encuesta.objects.order_by("-fecha_publ")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "encuestas/index.html", context)

def detalle(request, question_id):
    question = get_object_or_404(Encuesta, pk=question_id)
    return render(request, "encuestas/detalle.html", {"encuesta": question})

def resultados(request, question_id):
    question = get_object_or_404(Encuesta, pk=question_id)
    return render(request, "encuestas/resultados.html", {"encuesta": question})


def voto(request, question_id):
    question = get_object_or_404(Encuesta, pk=question_id)
    try:
        selected_choice = question.respuesta_set.get(pk=request.POST["respuesta"])
    except (KeyError, Respuesta.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "encuestas/detalle.html",
            {
                "encuesta": question,
                "error_message": "No seleccionaste una opción.",
            },
        )
    else:
        selected_choice.votos = F("votos") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("encuestas:resultados", args=(question.id,)))