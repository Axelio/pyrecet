from django.conf.urls import url

from recetas.views import RecetaView

urlpatterns = [
    url(r'^$', RecetaView.as_view(), name='receta'),
    ]

