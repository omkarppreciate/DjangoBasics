from django.http import JsonResponse

import json

def api_home(request,*args, **kwargs):

    # request -> HttpRequest -> Django
    #print(dir(request))
    # request.body

    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    print(request.GET)
    return JsonResponse(data)
