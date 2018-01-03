from django.shortcuts import render, get_object_or_404
from django.http import (HttpResponse,
                         HttpResponseForbidden)
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Product



def index(request):
    if request.method == 'GET':
        if 'next' in request.GET:
             next = request.GET['next']
        else:
            next = 'pointofsale/'

        context = {
            'Error': False,
            'next': next
            }
        return render(request, 'pointofsale/index.html', context=context)

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request,user)
        if next in request.GET:
            next = request.GET['next']
        else:
            next = 'pointofsale/order'
        return redirect(next)

    else:
        context = {
        'error': True
        }
        return render(request, 'pointofsale/index.html', context=context)


def order(request):
    list = Product.objects.all
    context = {
            'list': list,
    }
    return render(request, 'pointofsale/order.html', context=context)





