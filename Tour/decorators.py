from django.http import  HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs ):

    

        return view_func(request,*args,**kwargs)
    
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_fucn):
        def wrapper_func(request, *args,**kwargs):


            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_fucn(request,*args,**kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
             
            return view_fucn(request,*args,**kwargs)
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect()    
        if group == 'admin':
            return view_func(request,*args,**kwargs)
        

    return wrapper_function   