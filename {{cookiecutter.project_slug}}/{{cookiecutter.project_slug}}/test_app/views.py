from django.shortcuts import render
from django.views import View


class HomePageView(View):

    def get(self, request):
        return render(request, 'test_app/home.html')


home_page_view = HomePageView.as_view()
