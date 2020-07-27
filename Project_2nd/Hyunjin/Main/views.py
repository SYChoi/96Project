from django.shortcuts import render, redirect

def index(request):
	return render(request, 'main.html',)

def notice(request):
	return render(request, 'notice.html')

def antirust(request):
	return render(request, 'antirust_agent.html')

def equip(request):
	return render(request, 'equipment_craft.html')

def consulting(request):
	return render(request, 'consulting.html')

def online_consult(request):
	return render(request, 'online_consult.html')

def raw_mat(request):
	return render(request, 'raw_material.html')

def indust_part(request):
	return render(request, 'industrial_part.html')

def download(request):
	return render(request, 'download.html')

def engine_mat(request):
	return render(request, 'engine_material.html')

def BA(request):
	return render(request, 'business_area.html')
