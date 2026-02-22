from django.shortcuts import render

def home(request):
    return render(request, 'common/index.html', {'page_title': 'Carivio Home'})

def custom_404(request, exception):
    return render(request, '404.html', status=404)