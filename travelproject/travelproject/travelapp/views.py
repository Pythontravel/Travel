from django.shortcuts import render

from .models import place, team


# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request, 'index.html', {'result': obj, 'result1': obj1})

# def about(request):
#   return render(request, 'result.html')


# def contact(request):
# return HttpResponse('i am contact')


# def demo1(request):
#   name = "india"
#  return render(request, "home.html", {'obj': name})


# def operators(request):
# x = int(request.GET['num1'])
# y = int(request.GET['num2'])
# result = x + y
# result1 = x - y
# result2 = x * y
# result3 = x / y
# return render(request, "result.html", {'res': result, 'res1': result1, 'res2': result2, 'res3': result3})
