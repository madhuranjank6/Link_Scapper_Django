from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests 
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.
def scrape_links(request):
    if request.method == "POST":
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.content,'html.parser')
        for link in soup.find_all('a'):
            links_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=links_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        links_list = Link.objects.all()

    return render(request,'myapp/result.html',{'links_list':links_list})


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')