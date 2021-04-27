from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
# def firt_method(request,firstParametr):
#     output='<h2>first_method</h2> this paramether {0}'.format(firstParametr)
#     return HttpResponse(output,'firstFile.html')
# def secound_method(request,secondParametr):
#     output = '<h2>second_method</h2> this paramether {0}'.format(secondParametr)
#     return HttpResponse(output)
# def third_method(request,thirdParametr,id):
#     output = '<h2>third_method</h2> this paramether {0},id={1}'.format(thirdParametr,id)
#     return HttpResponse(output)
def Temp(request):
    return TemplateResponse(request,"test/body.html")
# Create your views here.

