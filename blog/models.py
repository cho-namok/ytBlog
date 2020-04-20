from django.db import models
from django.urls import reverse

# Create your models here.
#글의 분류(일상, 유머, 정보)
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex:일상)")

    def __str__(self):
        return self.name # 자기를 어떻게 표현할 것인가

#블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)#대표이미지 blank=True 비어 있을 수 있다
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True) #글을 작성하는 시점
    updateDate = models.DateTimeField(auto_now_add=True) #글을 수정하는 시점
    #하나의 글을 여러가지의 분류에 해당될 수 있다.(ex:정보, 유머), 
    #하나의 분류에는 여러가지 글이 포함될 수 있죠.(정보 카테고리에 글 10개)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.")

    def __str__(self):
        return self.title 

    # 자기 자신을 찾아오게 하는 주소
    # 1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)]) 

    def is_content_more300(self):
        return len(self.content) > 300 #글자 수가 300자 이상인가
    
    def get_content_under300(self):
        return self.content[:300] #300자 만큼 잘라서 표현