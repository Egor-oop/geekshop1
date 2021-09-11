from django.shortcuts import render


def index(request):
    context = {
        'title': 'Geekshop - Admin'
    }
    return render(request, 'admins/index.html', context)
