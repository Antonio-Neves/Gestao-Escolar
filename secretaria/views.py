from django.shortcuts import render


def index_secretaria_view(request):

	return render(request, 'secretaria/index-secretaria.html')
