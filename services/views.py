from django.http.response import HttpResponse

def services(request):
    return HttpResponse("choose your service")

def get_service(request, service):
    return HttpResponse(f"This page is for {service}.")
