#from django.shortcuts import render

#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.utils.decorators import method_decorator

#@method_decorator(csrf_exempt, name='admin')

def index(request):
    return HttpResponse("집가고싶다")
# Create your views here.
