from django.db.models import Q
from django.shortcuts import render

from .models import Journal


def filter_view(request):
    query = Journal.objects.all()
    title_contains_qs = request.GET.get('title_contains')
    id_exact_qs = request.GET.get('id_exact')
    title_author_qs = request.GET.get('title_author')

    if title_contains_qs != '' and title_contains_qs is not None:
        query = query.filter(title__icontains=title_contains_qs)

    elif id_exact_qs != '' and id_exact_qs is not None:
        query = query.filter(id=id_exact_qs)

    elif title_author_qs != '' and title_author_qs is not None:
        query = query.filter(Q(title__icontains=title_author_qs)
                             | Q(author__name__icontains=title_author_qs)
                             ).difference()

    context = {
        'query': query
    }
    return render(request, 'filter_form.html', context)
