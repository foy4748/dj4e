from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myview(request):
    # From Session
    from_session = request.session.get("from_session", 0)
    from_session = int(from_session) + 1
    request.session['from_session'] = from_session

    # From Cookie
    from_cookie = request.COOKIES.get("from_cookie",0)
    from_cookie = int(from_cookie) + 1
    request.COOKIES["from_cookie"] = from_cookie


    ctx = { "view_count": { "from_cookie": from_cookie, "from_session": from_session } }
    res = render(request, "hello/main.html", ctx)
    res.set_cookie("from_cookie", from_cookie)
    return res
