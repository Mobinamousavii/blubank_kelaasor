from django.http.response import HttpResponse, JsonResponse, FileResponse

def faq(request):
    return HttpResponse("You can read frequently asked question in this page")
