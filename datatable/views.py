from django.shortcuts import render, redirect

def datatable(request):
	return render(request, 'datatable/datatable.html')