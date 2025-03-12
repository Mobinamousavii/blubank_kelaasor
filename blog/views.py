from django.http.response import HttpResponse, JsonResponse, FileResponse

def blog(request):
    return HttpResponse("You can read blogs in this page.")

