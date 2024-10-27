from django.http import HttpResponse


def credits(request):
    content = "Nicky\nRony"

    return HttpResponse(content, content_type="text/plain")

