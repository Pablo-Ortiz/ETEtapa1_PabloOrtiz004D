from django.urls import path
from .views import Index, ingreso , lista, mod_partners, del_partners

urlpatterns = [

    path('', Index, name="Index"),
    path('ingreso', ingreso, name="ingreso"),
    path('lista', lista, name="lista"),
    path('mod_partners/<id>', mod_partners, name="mod_partners"),
    path('del_partners<id>', del_partners, name="del_partners")

    #metodos
]