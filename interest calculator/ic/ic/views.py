from django.http import HttpResponse
from django.shortcuts import render


def func1(request):
    return render(request, 'index.html')


def func2(request):
    amount = request.POST.get('a1', 'default')
    rate = request.POST.get('b1', 'default')
    time2 = request.POST.get('y', 'default')
    si = request.POST.get('si', 'off')
    ci = request.POST.get('ci', 'off')
    if si == "on":
        interest = (int(amount) * int(rate) * int(time2)) / 100
        interest2 = int(interest)
        param = {'amount1': amount, 'rate1': rate, 'time1': time2, 'si1': si, 'a': 'Simple interest + Amount',
                 'interest1': interest2}
        response = render(request, 'basic.html', param)
        return response
    elif ci == "on":
        a = int(amount) * pow(1 + int(rate) / 100, int(time2))
        interest = float(a) - int(amount)
        interest2 = float(interest)
        param = {'amount1': amount, 'rate1': rate, 'time1': time2, 'a': 'Compound interest + Amount', 'interest1': interest2}
        response = render(request, 'basic.html', param)
        return response
        print(a)
    else:
        return render (request,'basic.html',{'a':'Bad Credentials'})


def about(request):
    return render(request, 'about.html')


