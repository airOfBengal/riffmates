from django.http import HttpResponse, JsonResponse


def credits(request):
    content = "Nicky\nRony"

    return HttpResponse(content, content_type="text/plain")

def about(request):
    content = "<h1>This is my third attempt to be a Django Developer in 2024</h1>"
    return HttpResponse(content, content_type="text/html")


def version_info(request):
    content = {"version": 1.0}
    return JsonResponse(content, content_type="application/json")


