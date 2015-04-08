from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the tracker index.")
	
def cadet(request, xNumber):
    return HttpResponse("You're looking at cadet x%s." % xNumber)

def transportation(request, transpoID):
    response = "You're looking at the results of transportation %s."
    return HttpResponse(response % transpoID)

def user(request, userID):
    return HttpResponse("You're voting on user %s." % userID)