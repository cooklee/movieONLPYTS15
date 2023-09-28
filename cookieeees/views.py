from django.shortcuts import render
from django.views import View


# Create your views here.
class SetCookiesView(View):

    def get(self, request):
        return render(request, 'set_cookiee.html', )

    def post(self, request):

        http_response = render(request, 'ciasteczka.html', {'ciasteczka':request.COOKIES.items()})
        ciasteczko = request.POST.get('ciasteczko')
        wartosc = request.POST.get('wartosc')
        http_response.set_cookie(ciasteczko, wartosc)
        return http_response