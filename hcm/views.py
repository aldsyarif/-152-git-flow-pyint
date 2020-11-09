from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hcm.models import Okr, OkrOutput, KeyResult, Users


def index(request):
    getUsers = Users.objects.all()
    data = {
        'data': getUsers
    }

    return render(request, "index.html", data)
