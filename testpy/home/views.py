from django.http import HttpResponse

def home(request):
    print('welcome homepage')
    return HttpResponse("hello world 페이지 입니다")
