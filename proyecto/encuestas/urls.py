from django.urls import path

from . import views

app_name = "encuestas"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detalle, name="detalle"),
    path("<int:question_id>/resultados/", views.resultados, name="resultado"),
    path("<int:question_id>/voto/", views.voto, name="voto"),
]