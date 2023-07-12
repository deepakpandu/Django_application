from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_1.models import tech

# Create your views here.
def members(request):
    return HttpResponse("Hello world!")

def first(request):
  template = loader.get_template('try.html')
  return HttpResponse(template.render())

def All_data(request):
  mymembers = tech.objects.all().values()
  template = loader.get_template('all_data.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = tech.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
