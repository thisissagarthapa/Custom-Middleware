
from django.shortcuts import HttpResponse


""" class Mymiddleware:
    def __init__(self,get_response): 
        print("one time initialization")
        self.get_response=get_response
        print(self.get_response)
    
    def __call__(self,request):
        # code to be executed for each request before view and later middleware are called.
        print("this is before view")
        response=self.get_response(request)
        return response

 """


""" class BrotherMiddleware:
    def __init__ (self,get_response):
        self.get_response=get_response
        print("one time initialization")
    def __call__ (self,request):
        print("this is brother before view")
        response=self.get_response(request)
        print("this is brother after view")
        return 
    
class FatherMiddleware:
    def __init__ (self,get_response):
        self.get_response=get_response
        print("one time  initialization")
    def __call__ (self,request):
        print("this is father before view")
        response=self.get_response(request)
        print("this is father after view")
        return response
    
class MotherMiddleware:
    def __init__ (self,get_response):
        self.get_response=get_response
        print("one time initialization")
    def __call__ (self,request):
        print("this is Mother before view")
        response=self.get_response(request)
        print("this is Mother after view")
        return response """






# hooks Process-view

""" class Mymiddleware:
    def __init__(self,get_response): 
        print("one time initialization")
        self.get_response=get_response
        print(self.get_response)
    
    def __call__(self,request):
        # code to be executed for each request before view and later middleware are called.
        print("this is before view")
        response=self.get_response(request)
        return response
  
    # def process_view(request,*args,**kwargs):
    #     print("this is process view before view")
    #     return HttpResponse("this is before view")
    
    
    # def process_view(request,*args,**kwargs):
    #     print("this is process view before view")
    #     return None   #if returns None then the view will be called.
         """
         
         
# Exception handling through Middleware
""" class MyExceptionMiddleware:
    def __init__(self,get_response): 
        print("one time initialization")
        self.get_response=get_response
        print(self.get_response)
    
    def __call__(self,request):
        # code to be executed for each request before view and later middleware are called.
        print("this is before view")
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        print("exception occure")
        msg=str(exception)
        return HttpResponse(msg) """

# process_template_response
""" 
class MyTemplateResponse:
    def __init__(self,get_response): 
        print("one time initialization")
        self.get_response=get_response
        print(self.get_response)
    
    def __call__(self,request):
        # code to be executed for each request before view and later middleware are called.
        print("this is before view")
        response=self.get_response(request)
        return response
    def process_template_response(self,request,response):
        print("process template resonse from middleware")
        response.context_data["name"]="ramesh"
        response.context_data["age"]=25
        return response
    
 """