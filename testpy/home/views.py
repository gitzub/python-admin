from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group

# def home(request):
#     print('welcome homepage')
#     return HttpResponse("hello world 페이지 입니다")

def home(request):
        context = {
            "test1": Group,
            "test2": Group.objects.all(),
            "test3": Group.objects.get(name='test1'),
            "test4": Group.objects.values('name'),
            "test5": Group.objects.values_list('name'),
            "test6": Group.objects.filter(name='test1'),
            "test7": request.user.groups.name,
            "test8": request.user.username,
            "test9": request.user.is_superuser,
        }
        return render(request, 'test.html', context)