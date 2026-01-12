from django.shortcuts import render
from django.http import HttpResponse
from pandas import *
from numpy import *
# Create your views here.


pages = {
'home': 'home.html',
'servizi': 'servizi.html',
'perche_noi': 'perche_noi.html',
'pricing': 'pricing.html',
'settori': 'settori.html',
'chi_siamo': 'chi_siamo.html',
'contatti': 'contatti.html',
}


def home(request): return render(request, pages['home'])
def servizi(request): return render(request, pages['servizi'])
def perche_noi(request): return render(request, pages['perche_noi'])
def pricing(request): return render(request, pages['pricing'])
def settori(request): return render(request, pages['settori'])
def chi_siamo(request): return render(request, pages['chi_siamo'])
def contatti(request): return render(request, pages['contatti'])