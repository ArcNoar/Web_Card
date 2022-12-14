from django.http import HttpResponse
from django.shortcuts import redirect


def un_auth(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Main')
        else:
            return views_func(request, *args, **kwargs)
    return wrapper_func


def permited_unit(allowed_roles=[]):
    def decorator(views_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return views_func(request, *args, **kwargs)
            else:
                return HttpResponse('Insufficient role permit to acces this page.')
        return wrapper_func
    return decorator