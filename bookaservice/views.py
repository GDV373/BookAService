from django.shortcuts import render

# Create your views here.


def custom_500_handler(request, exception=None):
    return render(request, 'page_404.html', status=500)


def custom_error_handler(request, exception=None):
    if exception is None:
        return render(request, 'page_404.html', status=404)
    else:
        return render(request, 'page_404.html', status=404)
