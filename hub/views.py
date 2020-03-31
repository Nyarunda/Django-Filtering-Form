from django.shortcuts import render


def filter_view(request):
    return render(request, 'filter_form.html', {})
