from django.shortcuts import render
from .models import Parking
import subprocess
import time
# Create your views here.


def table_view(request):
    obj = Parking.objects.all()
    return render(request, 'table.html', {
        'obj_lst': obj,
    })
