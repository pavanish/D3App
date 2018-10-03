from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from django.http import JsonResponse
from django.core import serializers

import json
import random
import pandas as pd



def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
     if request.method == 'POST':
         form = DocumentForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             return redirect('home')
     else:
         form = DocumentForm()
     return render(request, 'core/model_form_upload.html', {
         'form': form
     })

def d3_data(request):
    #data = [50,100,150,200,250,130,210]
    data = random.sample(range(50, 300), 20)
    data_json= json.dumps(data)
    return render(request, 'core/d3Chart.html',{"data_json" : data_json})

def chordPlot(request):
    ChordData = [[11975,  5871, 8916, 2868],[ 1951, 10048, 2060, 6171],[ 8010, 16145, 8090, 8045],[ 1013,   990,  940, 6907]]
    #ChordData = [150,100,75,50,100,150,200,250,130,210]
    ChordData_json= json.dumps(ChordData)
    return render(request, 'core/chordDiagrame.html',{"ChordData_json" : ChordData_json})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        df = pd.read_csv(myfile)
        matrix = df.values.tolist()
        matrix_json = json.dumps(matrix)
        return render(request, 'core/chordDiagrame.html', {
            'matrix_json': matrix_json
        })
    return render(request, 'core/simple_upload.html')

def Ichord(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        df = pd.read_csv(myfile)
        df1 = pd.DataFrame({"name": df.columns, "color": randomColor(len(df.columns))})
        names = [{k: df1.values[i][v] for v, k in enumerate(df1.columns)} for i in range(len(df1))]
        #names = list(df.columns)
        names_json = json.dumps(names,ensure_ascii= False).encode('utf8')

        matrix = df.values.tolist()
        matrix_json = json.dumps(matrix)
        return render(request, 'core/IntChord.html', {
            'matrix_json': matrix_json,
            'names_json': names_json
        })
    return render(request, 'core/simple_upload.html')


def randomColor(n):
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(n)]
    return color

#clist = ["#000000","#800000","#008000","#808000","#000080","#800080","#008080","#c0c0c0","#808080","#ff0000","#00ff00","#ffff00","#0000ff","#ff00ff","#00ffff","#ffaf00","#ffd7d7","#d1fde9","#B10DC9","#FF4136","#4f45c0","#ffff66","#c4c1ea","#00cccc","#7c9d45","#57389f"]
#color= random.sample(clist, 15)