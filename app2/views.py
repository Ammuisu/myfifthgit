from django.shortcuts import render

# Create your views here.
def jinja_app2(request):
    d={"favfruit":"promogonet"}
    return render(request,'jinja_app2.html',context=d)