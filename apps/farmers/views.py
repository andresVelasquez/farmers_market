from django.shortcuts import render, redirect
import json # need this to use the json.loads method which takes the
# from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie

# Create your views here.

def index(request):
        return redirect('/main')

def show_fMarket(request):
    return render(request, 'farmers/index.html')

def localdata(request):
    return render(request, 'farmers/markets.json')

# @csrf_exempt # decorator to exempt route from CSRF checking. Not secure so don't use with sensitive data or routes that can have side effects.
def js2py(request):
    if request.method != "POST":
        return redirect("/main")
    global market # declare market a global variable
    # market = dict(request.POST.dict()) # changes querydict from POST response to dict. use this with form encoded data (I'm not using that here so do below instead)
    market = json.loads(request.body) # use this with json encoded data that has been stringified
    print "************************", market
    return redirect("/marketwall")

def marketwall(request):
    return render(request, "farmers/marketwall.html", market)
