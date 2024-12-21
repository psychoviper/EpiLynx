from django.shortcuts import render, redirect
from django.conf import settings
import os
from django.http import HttpResponseRedirect
from collections import defaultdict
from .logic import score
from .segregation import segregate
from .protparam import fetch_instability
from .linking import link
from .models import LinkerForm
import pandas as pd
from django.http import HttpResponse
import colorsys

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Select a CSV File',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'style': 'border: 2px solid #007bff; padding: 10px;',
            'placeholder': 'Choose file'
        })
    )

#  Create your views here.
# epitopes={
#     1:["DEPPPPKSSRVTASAPSP","ISDDSDDEPPPPKSSRVT"],
#     2:["ISDDSDDEPPPPKSSRVT","IYSESPFYRPVLLLRDVQ"],
#     3:["IYSESPFYRPVLLLRDVQ","MTDPLAGAM"],
#     4:["MTDPLAGAM","ITKCVPHCY"],
#     5:["ITKCVPHCY","STDGSALPA"],
#     6:["STDGSALPA","AAAAMQILVSKELDG"],
#     7:["AAAAMQILVSKELDG","AAGTWKTERVITSPQ"],
#     8:["AAGTWKTERVITSPQ","ANAAIFETLLTPEDC"],
# }

epitopes=defaultdict(list)

linkers={
    1:['EAAK',0],
    2:["GSGS",0],
    3:["GPGP",0],
    4:["GGGS",0],
}

vaccine=""
state=1

cache=defaultdict(str)

def index(request):
    global epitopes
    if request.method == 'POST':
        print(request.POST)
        if request.FILES:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                # Read the uploaded CSV file
                csv_file = request.FILES['file']
                try:
                    df = pd.read_csv(csv_file)
                    b_cell, ctl_cell, htl_cell = segregate(df)
                    return render(request, 'epilynx/selection.html', {'b':b_cell,'c':ctl_cell,'h':htl_cell})
                except Exception as e:
                    return HttpResponse(f"Error reading the file: {e}")
        else:
            ep=[]
            if(request.POST.get('adjuvant')):
                adjuvant=request.POST.get('adjuvant')
                ep.append(adjuvant)
            for linker in request.POST.getlist('selected-b-items'):
                ep.append(linker)
            for linker in request.POST.getlist('selected-c-items'):
                ep.append(linker)
            for linker in request.POST.getlist('selected-h-items'):
                ep.append(linker)
            for i in range(1,len(ep)):
                epitopes[i]=[ep[i-1],ep[i]]
            if(request.POST['radioOption']=='option1'):
                return redirect(linking)
            else:
                preferred_linkers=pruning(epitopes)
                n=int(request.POST.get('number'))
                result = link(epitopes,preferred_linkers,n)
                df1 = pd.DataFrame(columns=["instability_Index",'Sequence'])
                for i, seq in enumerate(result):
                    x = round(score(seq),3)
                    df1.loc[i]=[x,seq]
                df1 = df1.sort_values(by="instability_Index")
                file_path = os.path.join(settings.MEDIA_ROOT, "sorted_data.csv")
                df1.to_csv(file_path, index=False)
                return render(request,'epilynx/display_constructs.html',{"data":df1, "file_name":"sorted_data.csv"})

            # return HttpResponse(f"Done selection B")

    else:
        form = UploadFileForm()
    print('here again')
    return render(request, 'epilynx/index.html', {'form': form})

def pruning(epitopes):
    preferred_linkers=defaultdict(list)
    for key, epitope in epitopes.items():
        for linker in linkers.values():
            string = epitope[0] + linker[0] + epitope[1]
            preferred_linkers[key].append((linker[0],score(string)))
    for key in preferred_linkers:
        preferred_linkers[key]=sorted(preferred_linkers[key], key=lambda x: x[1])
    print(preferred_linkers)
    return preferred_linkers


def cal_linker_score():
    
    scores=[]
    for key in linkers:
        string = epitopes[state][0] + linkers[key][0] + epitopes[state][1]
        scores.append(score(string))

        # Extract scores for normalization
    # scores = [value[1] for value in linkers.values()]

    # Compute max and min scores
    max_score = max(scores)
    min_score = min(scores)

    # Normalize scores
    for i,key in enumerate(linkers):
        normalized_score = (scores[i] - min_score) / (max_score - min_score) if max_score != min_score else 0.5
        hue = (1.0 - normalized_score) * 0.4  # Green (0.4) to Red (0.0)
        saturation = 0.7
        brightness = 0.9
        rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
        hex_color = '#{:02x}{:02x}{:02x}'.format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255),
        )
        # red = (1 - normalized_score) * 255  # Red decreases as score increases
        # green=normalized_score * 255    # Green increases as score increases
        # blue=0   
        linkers[key][1]=hex_color
    # print(linkers)
    return linkers


def generate_gradient_color(score, min_score, max_score):
    normalized = (score - min_score) / (max_score - min_score)
    hue = (1.0 - normalized) * 0.4  # Green (0.4) to Red (0.0)
    saturation = 0.7
    brightness = 0.9

    rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
    hex_color = '#{:02x}{:02x}{:02x}'.format(
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255),
    )
    return hex_color


def linking(request):
    global vaccine, state, cache
    linkerform = LinkerForm()
    # print(type(linker_score))
    print(request.POST)
    if request.method == "POST":
        state = int(request.POST['serial_index'])
        linkers=cal_linker_score()
        print("state:",state)
        # linker_id = int(request.POST['linker'])
        linker=request.POST['selected_linker']
        new=defaultdict(str)
        if(state==1):
            cache.clear()
            cache[state]=epitopes[state][0]+linker+epitopes[state][1]
        else:
            # for i in range(state):
            #     new[i+1]=cache[i+1]
            # cache=new.copy()
            cache[state]=cache[state-1]+linker+epitopes[state][1]
        print(cache)
        instability=round(score(cache[state]),3)
        state+=1
        if(state>len(epitopes)):
            print(len(epitopes),state)
            return render(request, 'epilynx/linker.html',{'forms': linkerform, 'message':"completed",'vaccine':cache[state-1],'score':instability,'index':state,'stages':range(1,len(epitopes)+1),})
        else:
            print(linkers.values())
            return render(request, 'epilynx/linker.html',{'forms':linkerform, 'epitope1':epitopes[state][0],'epitope2':epitopes[state][1],"linkers":linkers,'vaccine':cache[state-1],'score':instability,"index":state,'stages':range(1,len(epitopes)+1),})
    else:
        state = 1
        linkers=cal_linker_score()
        print(len(linkers[1]))
        return render(request, 'epilynx/linker.html',{'forms': linkerform, 'epitope1':epitopes[state][0],'epitope2':epitopes[state][1], 'linkers': linkers,'index':state,'stages':range(1,len(epitopes)+1)})   