from django.http import HttpResponse

def helloworldfunc(request):
    return HttpResponse('hello world')