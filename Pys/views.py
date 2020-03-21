# http://127.0.0.1:8000/app/1/?name=adduser&uid=911556872&username=ddd6dddddd&akey=sdd&vkey=1000
# sudo chmod 777 -R /mnt
# sudo su - postgres
# pg_dumpall > /mnt/baas1/AllPgDatabases.Backup
# sudo tar -czvf /mnt/backup.tar.gz /mnt/*

#/mnt/baas1
# sudo python3 manage.py runserver

from django.http import HttpResponse
import json
import urllib.parse
import random
import psycopg2

con = psycopg2.connect("dbname=DB1 user=postgres host=localhost password=postgres port=5432")
cur = con.cursor()

def app(request):
    # re = apps1(request.method, request.GET.get('name'), request.GET.get('uid'), request.GET.get('akey'), request.GET.get('vkey'), json.dumps(dict(request.GET.items())))
    apname = request.GET.get('name')
    js = json.dumps(dict(request.GET.items()))
    try:

      if apname in ['adduser','deluser']:  cur.execute("select pub1.ap_addusr1 ('%s')" % (js))
      elif apname in ['a','b']:            cur.execute("select pub1.ap_addusr1 ('%s')" % (js))
      elif apname in ['c','d']:            cur.execute("select pub1.ap_addusr1 ('%s')" % (js))
      else: raise Exception('error appname: ' + apname)

      con.commit()
      re = json.dumps(cur.fetchall())
    except Exception as e:
      con.rollback()
      re = str (e)
    finally:
      pass

    return HttpResponse (re)      # request.GET.items()

def sendSMS (apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender, 'test': 'test'})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def index(request):
    rn = "Shiva Verification Code: " + str (random.randint(10000, 99999))
#    resp = sendSMS('LGtAP6X5k0s-rrTVpmw5dZDX3JS1i2zp5qWcPQhROH', '00989126787542', 'soheil', rn)
    resp = rn;
    return HttpResponse(resp)
#    return HttpResponse("Hello, world. You're at the polls index.")


