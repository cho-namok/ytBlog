#유튜브 블로그 만들기 강의
pip install virtualenv
ok@ok-Samsung:~/myboard$ sudo apt-get update
ok@ok-Samsung:~/myboard$ sudo apt-get install python3-venv
ok@ok-Samsung:~/myboard$ python3 -m venv venv
ok@ok-Samsung:~/myboard$ source myvenv/bin/activate
ok@ok-Samsung:~/myboard$ pip install --upgrade pip

ok@ok-Samsung:~/myboard$ pip3 install django
(myvenv) ok@ok-Samsung:~/myboard/mysite$ pip3 install django-widget-tweaks #글 작성을 디자인 꾸미기 위해
(myvenv) ok@ok-Samsung:~/myboard/mysite$ pip3 install pillow #그림 파일을 사용하기 위해 설치
(venv) ok@ok-Samsung:~/myboard$ python3 -m pip install -U pylint

(venv) ok@ok-Samsung:~/myboard$ django-admin startproject mysite
(venv) ok@ok-Samsung:~/myboard$ cd mysite
(venv) ok@ok-Samsung:~/myboard$ django-admin startapp blog
(venv) ok@ok-Samsung:~/myboard$ python3 manage.py makemigrations
(venv) ok@ok-Samsung:~/myboard/svcbr$ python3 manage.py migrate
(venv) ok@ok-Samsung:~/myboard$ python3 manage.py runserver
 
-------------------------------------
(myvenv) ok@ok-Samsung:~/myboard/mysite$ git init
/home/ok/myboard/mysite/.git/ 안의 빈 깃 저장소를 다시 초기화했습니다
(myvenv) ok@ok-Samsung:~/myboard/mysite$ git config --global user.name "cho-namok"
(myvenv) ok@ok-Samsung:~/myboard/mysite$ git config --global user.email ican1472@gmail.com
----------------------------------------------------------------------------

mysite/settings.py에 앱 등록
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
]

TIME_ZONE = 'Asia/Seoul'


그 다음 mysite/urls.py 파일에 모듈을 연결
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', RedirectView.as_view(url='/blog/', permanent=True))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

blog 폴더에 urls 파일 생성
from django.urls import path
from blog import views

urlpatterns =[
    path("", views.index, name="index")
]

blog/views.py 에 index 함수를 만들어 준다

from django.shortcuts import render

def index(req):
    context = {

    }
    #index를 호출하면 index.html로 context=context로 넘겨주겠다
    return render(req, "index.html", context=context) 

blog 폴더 안에 templates라는 폴더를 만든다
templates 폴더 안에 index.html 파일을 만든다

index.html 폴더 안에서 doc 입력하고 tab 키를 누르면 html 기본구조가 입력된다
mysite/blog/templsates/index.html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>

(base) ~/myboard/mysite$ python manage.py makemigrations #데이터 모델 변경점 확인
(base) ~/myboard/mysite$ python manage.py migrate # 데이터 모델 db에 반영

~/myboard/mysite$ python manage.py runserver

mysite/static 폴더를 만들고 그 안에 test.js 파일을 만듦
alert('환영합니다.~')

mysite/blog/templsates/index.html
<body>
    <h2> hi~~</h2>
    {% load static %} <!-- static 파일 쓰기 전에 선언해야 함-->
    <script src= "{% static 'js/test.js' %}"></script>
</body>

mysite/settings.py에
STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

https://colorlib.com/wp/template/suppablog/
다운 받아 압축을 풀고 파일 가운데 style.css를 css 폴더 안에 붙여 넣는다
css, demo-images, fonts, images, js 폴더를 복사하여 mysite/static/폴더 안에 붙여넣는다
index.html과 single.html을 복사하여 mysite/blog/templates/ 안에 붙여 넣는다

https://github.com/netscout/chocopy/blob/master/How-to/django-blog/replace_txt.py
mysite/blog/templates/replace_txt.py 파일을 만들고 위 사이트 내용을 복사해서 붙여넣는다고 저장한다

터미널 창에서 templates폴더로 이동하여 다음 작업을 실행함
(myvenv) (base) ~/myboard/mysite/blog/templates$ python replace_txt.py
mysite/blog/templates/ 아래에 index.html와, single.html의 
href='{% static "css/style.css" %}' /> 부분과 
{% load static %}을 static 앞 부분을 수정한다

github 사이트에서 featured-image.jpg, image.jpg, 복사하여 static/demo-images 안에 붙여넣는다

/blog/urls.py에 
urlpatterns =[
    path("", views.index, name="index"),
    path("single/", views.single, name="single")
]
/blog/views.py 안에
def single(req):
    context = {

    }
    #index를 호출하면 index.html로 context=context로 넘겨주겠다
    return render(req, "single.html", context=context) 

index.html
ctrl+f single.html 찾아 {% url 'simgle' %}바꾸기를 함

#bootstrap인터넷에서 검색하여 css와 js 복사하여  index.html에 붙여넣기 한다.