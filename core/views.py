from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Olá {} sua idade é {} </h1>'.format(nome, idade))


def soma(request, valor1, valor2):
    total = valor1 + valor2
    return HttpResponse('<h1>Total {} </h1>'.format(total))


def multiplicacao(request, valor1, valor2):
    total = valor1 * valor2
    return HttpResponse('<h1>Total {} </h1>'.format(total))


def subtracao(request, valor1, valor2):
    total = valor1 - valor2
    return HttpResponse('<h1>Total {} </h1>'.format(total))


def divisao(request, valor1, valor2):
    total = valor1 / valor2
    return HttpResponse('<h1>Total {} </h1>'.format(total))
