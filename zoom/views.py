from multiprocessing import context
from django.shortcuts import redirect, render

# Controller methods
from zoom.controller import CreateMeeting, GetAccessToken, GetAuthorizationUrl, GetUserDetails, RedirectToErrorPage

# Create your views here.

# Home Route with client auth url
def index(request):

    # Client Auth Url
    data = {
        'zoomAuthUrl': GetAuthorizationUrl()
    }
    return render(request, 'zoom/index.html',data)

# Meeting Route
def Meeting(request):
    
    # Create meeting
    data,status=CreateMeeting(request)
    
    # Status 201:refers that meeting is successfully created
    if(status!=201):
        return RedirectToErrorPage(data["reason"])
    else:
        try:
            # Meeting details
            context={
            "meeting_topic": data["topic"],
            "start_meeting": data["start_url"],
            "join_meeting": data["join_url"],
            }
            return render(request, 'zoom/meeting.html',context)
        
        except:
            return RedirectToErrorPage("Unable to create meeting.")


# Dashboard Route with access token
def Dashboard(request):

    # Get user
    data,status=GetUserDetails(request)

    # Status 200:refers that user is exist and fetched
    if(status!=200):
        return RedirectToErrorPage(data["message"])

    else:
        try:
             # User details
            context = {
        'first_name': data["first_name"],
        'accessToken':data["accesstoken"]
            }

            return render(request, 'zoom/dashboard.html',context)
        except:
            return RedirectToErrorPage("Unable to get details of the user")

# Handle Callback responded by client
def HandleCallback(request):

    # Get access token to use zoom services
    data,status=GetAccessToken(request)

    # status 200: refers user get access token
    if(status!=200):
        return RedirectToErrorPage(data["reason"])
    else:
        try:
            accessToken=data["access_token"]
            context = {
            'accessToken':data["access_token"]
            }
            return redirect('/dashboard?accesstoken={0}'.format(accessToken),data=context)
        except:
            return RedirectToErrorPage("invalid access token")

# Error Route
def error(request):

    # Get error message from url query
    errorMessage=request.GET.get('message', '')

    data = {
        'error': errorMessage
    }
    return render(request, 'zoom/error.html',data)