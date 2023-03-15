from django.shortcuts import render

# Create your views here.
def Conditional(request):
    D={'a':10,'b':30}
    return render(request,'Conditional.html',D)

def conditional1(request):
    d={'a':20,'b':50,'c':90,'n':'chandu'}
    return render(request,'conditional1.html',d)