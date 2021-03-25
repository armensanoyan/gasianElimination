from scipy.integrate import quad
import math
import matplotlib.pyplot as plt
import numpy as np

from django.shortcuts import render
from django.http import HttpResponse

from .utils import matsum
from .utils import elimination, generate

def Index(request):
    context = {}
    if request.method == 'POST':
        x1 = float(request.POST['x1'])
        x2 =float( request.POST['x2'])
        mid = float(request.POST['mean'])
        sg = float(request.POST['sigma'])
        x_Array = np.linspace(x1, x2, 1000)

        def normpdf(x):
            var = float(sg)**2
            denom = (2*math.pi*var)**.5
            num = math.exp(-(float(x)-float(mid))**2/(2*var))
            return num/denom

        totul_pdf = quad(normpdf, x1, x2)
        y_Array = [normpdf(x) for x in x_Array]
        context = {
            'result': totul_pdf[0],
            'error': totul_pdf[1]
        }
    return render(request, 'gaus_app/index.html', context)

def Count_Matrix(request):
    result = ''
    if request.method == 'POST':
        X = [e.replace('x','') for (e,v) in request.POST.items() if e.startswith('x')]
        Y = [e.replace('y','') for (e,v) in request.POST.items() if e.startswith('y')]

        m1 = [[ int(request.POST['x' + str(i) + str(j)]) for j in range(int(request.POST['first_y']))] for i in range(int(request.POST['first_x']))]
        m2 = [[ int(request.POST['y' + str(i) + str(j)]) for j in range(int(request.POST['first_y']))] for i in range(int(request.POST['first_x']))]
        operation =  request.POST['operation']
        result = matsum(m1, m2, operation)

        print('result', result)
        print('operation', operation)

    context = get_context(4)
    return render(request, 'gaus_app/matrix.html', context)

def get_context(dimantion):
    return {
        'x': list(range(dimantion)),
        'y': list(range(dimantion+1)),
        'x_length':dimantion,
        'y_length':dimantion+1,
    }

def Get_matrix(request):
    
    if request.method == 'POST':
        post = request.POST
        A = [[ int(request.POST[str(e)+str(i)]) for i in range(int(post['x'])+1)] for e in range(int(post['x']))]  
        gauss_elim = elimination(A)
        
        dimantion = int(post['x'])
        context = get_context(dimantion)
        
        context['result'] = gauss_elim['result']
        context['error'] = gauss_elim['error']
        return render(request, 'gaus_app/get_matrix.html', context)
    else:
        dimantion = 3 
        context = get_context(dimantion)
    return render(request, 'gaus_app/get_matrix.html', context)

def Change_dir(request):
    dim = int(request.POST['x'] if request.POST['x'] else 3)
    context = get_context(dim)
    return render(request, 'gaus_app/get_matrix.html', context)