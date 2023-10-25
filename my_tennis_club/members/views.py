from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('stay.html')
    return HttpResponse(template.render())

def stay(request):
    template = loader.get_template('stay.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

def portofolio(request):
    template = loader.get_template('portofolio.html')
    return HttpResponse(template.render())
    
def uim(request):
    template = loader.get_template('uim.html')
    return HttpResponse(template.render())

def instagram(request):
    template = loader.get_template('instagram.html')
    return HttpResponse(template.render())


def hadiah(request):
    template = loader.get_template('hadiah.html')
    return HttpResponse(template.render())
