from django.shortcuts import render, redirect
from django.http import Http404
from Main.models import Post
#from Main.forms import PostForm

def index(request):
	return render(request, 'main.html')

def greeting(request):
        return render(request, 'greeting.html')

def contact(request):
	return render(request, 'contact.html')

def notice(request):
	posts = Post.objects.all()
	return render(request, 'notice.html', {'posts': posts})

def notice_detail(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except:
		raise Http404('해당 게시물을 찾을 수 없습니다.')
	return render(request, 'notice_detail.html', {'post': post})
"""
def notice_create(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			return notice(request)
	else:
		form = PostForm
		pw = "123"
		return render(request, 'notice_create.html', {'form': form, 'pw': pw})
"""
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

def engine_mat(request):
	return render(request, 'engine_material.html')

def BA(request):
	return render(request, 'business_area.html')

def antirust_detail(request):
        return render(request, 'antirust_detail.html')
