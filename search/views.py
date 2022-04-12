from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def index(request):
    word = 'beer'
    URL = f"https://www.google.com/search?q={word}&hl=en&tbm=isch&sxsrf=APq-WBuA7q3iIcAKMj5STRT6RWG0vAWlkQ%3A1649731337548&source=hp&biw=1242&bih=561&ei=CedUYsTYEbPP0PEP6PKJ6AM&iflsig=AHkkrS4AAAAAYlT1Ga52bdPmzFCJXpOGUvGxPDFrR-em&ved=0ahUKEwiEgdaSwI33AhWzJzQIHWh5Aj0Q4dUDCAc&uact=5&oq=jdm&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6CggjEO8DEOoCECc6CAgAELEDEIMBOgUIABCABFDsOViCPWCzP2gCcAB4AIABOogB1wGSAQE0mAEAoAEBqgELZ3dzLXdpei1pbWewAQo&sclient=img"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    print(page.text)
    return HttpResponse(page.text)
