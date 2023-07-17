from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from app_1.models import tech

# Create your views here.
def members(request):
    return HttpResponse("Hello world!")

def first(request):
  mymembers = tech.objects.all()[0]
  template = loader.get_template('try.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

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


def All_in_one(request):
  template = loader.get_template('template.html')
#   context = {
#     'all_in_one': ['Deepak', 'Raj', 'shubham'],   
#   }
  return HttpResponse(template.render())




def testing(request):
  mymembers = tech.objects.all().values()
  template = loader.get_template('try.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def testing_1(request):
  template = loader.get_template('try_1.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
  }
  return HttpResponse(template.render(context, request))

def Footer(request):
  template = loader.get_template('footer.html')
  return HttpResponse(template.render())

def All_in_one_1(request):
  template = loader.get_template('try_with.html')
  context = {
    'all_in_one': ['Deepak', 'Raj', 'shubham'],   
  }
  return HttpResponse(template.render(context, request))

