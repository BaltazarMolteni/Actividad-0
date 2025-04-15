from django.urls import path

from . import views

app_name = "encuestas"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detalle"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="resultados"),
    path("<int:question_id>/voto/", views.voto, name="voto"),
]