from django.shortcuts import render, get_object_or_404
from .models import Programmes

# Create your views here.


def all_programmes(request):
    """A view to show all programmes"""

    programmes = Programmes.objects.all()

    context = {
        'programmes': programmes,
    }

    return render(request, 'programmes/programmes.html', context)


def programme_detail(request, programme_id):
    """ A view to show individual programme details """

    programme = get_object_or_404(Programmes, pk=programme_id)

    context = {
        'programme': programme,
    }

    return render(request, 'programmes/programme_detail.html', context)
