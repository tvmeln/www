from django.shortcuts import render


def main(request):
    context = {'y': range(9)}
    return render(request, 'main/main.html', context)
