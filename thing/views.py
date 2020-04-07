from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Thing, Comment
from .forms import ThingForm, CommentForm
from django.contrib.auth.models import User
import user_agents

def main(request):
    return render(request, 'main.html')

def add(request):
    if request.method == 'GET':
        form = ThingForm()
        return render(request, 'add.html', {'form' : form})
    elif request.method == 'POST':
        form = ThingForm(request.POST or None, request.FILES or None)
        if form.is_valid(): form.save()
        return redirect('/see')

def see(request):
    if request.method == 'GET':
        things = Thing.objects.filter(add = True)
        things = things[::-1]
        things = things[:5]
        pages = len(things) // 5 + 1 if len(things) % 5 == 0 else len(things) // 5
        pm = []
        for i in range(1, pages+1):
            pm.append(i)
    elif request.method == 'POST':
        things = []
        req = request.POST['name'].lower()
        for i in Thing.objects.all():
            if req in i.title.lower():
                things.append(i)
            elif req in i.text.lower():
                things.append(i)
        pages = len(things) // 5 + 1 if len(things) % 5 == 0 else len(things) // 5
        pm = []
        for i in range(1, pages+1):
            pm.append(i)
    return render(request, 'see.html', {'things' : things, 'pages' : pm})

def page_by_id(request, id):
    things = Thing.objects.filter(add = True)
    things = things[id * 5 - 5:id * 5]
    things = things[::-1]
    pages = len(things) // 5 + 1 if len(things) % 5 == 0 else len(things) // 5
    pm = []
    for i in range(1, pages+1):
        pm.append(i)
    return render(request, 'see.html', {'things' : things, 'pages' : pm})


def by_id(request, id):
    thing = Thing.objects.get(id = id)
    comments = Comment.objects.filter(thing = id)
    if request.method == 'GET':
        return render(request, 'by_id.html', {'thing' : thing, 'comments' : comments})
    elif request.method == 'POST':
        try:
            author = request.user
            text = request.POST['text']
            comment = Comment(thing = thing, author = author, text = text)
            comment.save()
            return render(request, 'by_id.html', {'thing' : thing, 'comments' : comments})
        except:
            return redirect('accounts/signup')

def by_tag(request, tag):
    things = Thing.objects.filter(tag = tag, add = True)
    return render(request, 'by_tag.html', {'things' : things})

def meta(request):
    meta = request.META.items()
    try: ip = request.META['HTTP_X_FORWARDED_FOR']
    except: ip = request.META['REMOTE_ADDR']
    req = request.META['REQUEST_METHOD']
    requrl = request.META['REQUEST_URI']
    server_protocol = request.META['SERVER_PROTOCOL']
    data = request.META['HTTP_USER_AGENT']
    user_agent = data
    data = user_agents.parse(data)
    port = request.META['REMOTE_PORT']
    formats = request.META['HTTP_ACCEPT_ENCODING']
    accerp_lang = request.META['HTTP_ACCEPT_LANGUAGE']
    mime = request.META['HTTP_ACCEPT']
    try:
        cookie = request.META['HTTP_ACCEPT'] if cookie else 'Нет'
    except: cookie = 'Нет'
    return render(request, 'meta.html', {
                                            'meta' : meta,
                                            'ip' : ip,
                                            'req' : req,
                                            'request_url' : requrl ,
                                            'protocol' : server_protocol,
                                            'browser' : data.browser.family+' '+data.browser.version_string,
                                            'os' : data.os.family+' '+data.os.version_string,
                                            'port' : port,
                                            'user_agent' : user_agent,
                                            'formats' : formats,
                                            'langs' : accerp_lang,
                                            'mime' : mime,
                                            'cookie' : cookie,
                                            'mob' : True if ('iOS' in data.os.family) or ('Android' in data.os.family) else False
                                        })