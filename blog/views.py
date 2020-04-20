from django.shortcuts import render
from blog.models import Category, Post #카테고리 작성 위해
from django.views import generic #상세보기 하기 
from django.contrib.auth.mixins import LoginRequiredMixin #글 작성하기 위해
from django.views.generic.edit import CreateView # 로그인 한 사람만

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest
    }
    #index를 호출하면 index.html로 context=context로 넘겨주겠다
    return render(req, "index.html", context=context)

class PostDetailView(generic.DetailView):
    model = Post #상세한 내용을 볼때 작성

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    #어떤 필드에 대하여 글을 작성할 것인가
    fields = ["title", "title_image", "content", "category"] 