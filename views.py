from django.http import HttpResponse
import json
import urllib.request
import urllib.parse
import random
import psycopg2

con = psycopg2.connect(database='DB1', user='postgres', password='postgres')
cur = con.cursor()

# http://127.0.0.1:8000/app/?name=adduser&uid=9126787542&akey=sdd&vkey=1000

def app(request):
#    return HttpResponse(request.text)
    re = apps1('GET', request.GET.get('name'), request.GET.get('uid'), request.GET.get('akey'), request.GET.get('vkey'), '{}')
    return HttpResponse (re)      # request.GET.items()

def apps1 (kind, name, uid, akey, vkey, js):
    cur.execute("select apps1 ('%s', '%s', %s, '%s', %s, '%s')" % (kind, name, uid, akey, vkey, js))
    con.commit()
    re = json.dumps (cur.fetchall())
    return (re)
#    cur.execute("insert into user1 (id, username) values (50391898, '*192484')")
#    con.close()

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

