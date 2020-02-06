from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
import json
from .forms import PostForm
from django.utils import timezone
from .models import Post
# Create your views here.
def home(request):
	return render(request, 'sec/home.html')

def fir_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('fir_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'sec/fir_fill.html', {'form': form})



def fir_list(request):
	posts = get_list_or_404(Post)
	return render(request, 'sec/fir_list.html', {'posts':posts})

def fir_new_api(request):
	if request.method == "POST":
		y = json.loads(request.body)
		username = y["name"]
		desc = y["details"]
		title = y["title"]
		try:
			post = Post.objects.create(author = username, title = title, text = desc)
			data = {
				"message": "successful"
			}
			return JsonResponse(data, safe=False)
		except:
			data = {
				"message": "Incorrect details!"
			}
			return JsonResponse(data, safe=False)
	else:
		data = {
			"message": "Incorrect details!"
		}
		return JsonResponse(data, safe=False)



def fir_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
    # print(obj_id,'  ', content_type)
	return render(request, 'sec/fir_detail.html', {'post': post})

def fir_detail_api(request):
	if request.method == 'POST':
		y = json.loads(request.body)
		reportID = y["id"]
		try:
			post = Post.objects.get(pk=reportID)
			data = {
				"title": post.title,
				"description": post.text,
				"author": post.author
			}
			return JsonResponse(data, safe=False)
		except:
			data = {
				"message": "Incorrect details!"
			}
			return JsonResponse(data, safe=False)
	else:
		data = {
			"message": "Incorrect details!"
		}
		return JsonResponse(data, safe=False)