from django.http import HttpResponse
import json
import urllib.request
import urllib.parse
import random

# http://127.0.0.1:8000/polls/app/?name=adduser&num=09126787542&print=true&T=Ali%20reza

def app(request):
#    j = json.loads(request.body)
#    return HttpResponse(request.GET.get('T'))
    return HttpResponse(request.GET.items())


def sendSMS (apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender, 'test': 'test'})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def index(request):
    rn = "Shiva Verification Code: " + str (random.randint(10000,99999))
    resp = sendSMS('LGtAP6X5k0s-rrTVpmw5dZDX3JS1i2zp5qWcPQhROH', '00989126787542', 'soheil', rn)
    return HttpResponse(resp)

