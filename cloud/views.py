from http.client import HTTPResponse
from urllib.error import HTTPError
from . import config
import json
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import joblib

# Create your views here.

from django.http import HttpResponse

global vari

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")()

@csrf_exempt
def getCPUUsage(request):
    if request.method == 'POST':
        print(request)
        jsonBody=json.loads(request.body.decode('utf-8'))
        if config.model!=None:
            f=[float(jsonBody['day1'])]
            s=[float(jsonBody['day2'])]
            t=[float(jsonBody['day3'])]
            inp=[f,s,t]
            scaler=joblib.load('scalar_model_avg_cpu.save')
            vals=scaler.transform(inp)
            inps=[vals]
            arr=np.array(inps,dtype='float32')
            res=config.model.predict(arr)
            res=scaler.inverse_transform(res)
            res=str(res[0][0])
            return JsonResponse({'res':res})
            



def LoadModel():
    if config.model==None:
        from keras.models import load_model
        config.model=load_model('model_avg_cpu.h5')


        



        

    
