from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Encuesta, Respuesta
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = "encuestas/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Encuesta.objects.order_by("-fecha_publ")[:5]


class DetailView(generic.DetailView):
    model = Encuesta
    template_name = "encuestas/detalle.html"


class ResultsView(generic.DetailView):
    model = Encuesta
    template_name = "encuestas/resultados.html"

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