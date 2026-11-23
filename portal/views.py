from django.shortcuts import render
from portal.zadanie1.stolowka import wyniki_stolowka
from portal.zadanie2.pracownie import wyniki_pracownie
from portal.zadanie3.dziennik import wyniki_dziennik


def raport(request):
    context = {
        "stolowka": wyniki_stolowka(),
        "pracownie": wyniki_pracownie(),
        "dziennik": wyniki_dziennik(),
    }
    return render(request, "portal/raport.html", context)