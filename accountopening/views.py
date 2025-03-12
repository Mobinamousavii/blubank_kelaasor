from django.http.response import HttpResponse, JsonResponse, FileResponse

def account_opening(request):
    return HttpResponse("You can open your acount here.")
