from django.http import HttpResponse


def index(request):
    return HttpResponse('Main page')


def ice_cream_list(request):
    return HttpResponse('Ice cream list')


# In the url we are waiting for a parameter, and we need to pass it into a function to use
def ice_cream_detail(request, pk):
    return HttpResponse(f'Ice cream No. {pk}')
