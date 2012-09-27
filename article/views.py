from django.http import HttpResponseRedirect
# Create your views here.

def temp(request):
	print('in temp')
	return HttpResponseRedirect('http://www.google.com')
