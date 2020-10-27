from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}. Você tem {idade} anos.</h1>')

def soma(requests, num1, num2):
    return HttpResponse(f'<h1 color=red>{num1} + {num2} = {num1+num2}</h1>')

def subtracao(requests, num1, num2):
    return HttpResponse(f'<h1>{num1} - {num2} = {num1-num2}</h1>')

def multiplicacao(requests, num1, num2):
    return HttpResponse(f'<h1>{num1} x {num2} = {num1*num2}</h1>')

def divisao(requests, num1, num2):
    return HttpResponse(f'<h1>{num1} ÷ {num2} = {num1/num2}</h1>')
