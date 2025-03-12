from django.http.response import HttpResponse, JsonResponse, FileResponse

def about(request):
    return HttpResponse("You can read about us in this page.")

