from django.http import HttpResponseRedirect
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from shorter.models import Token
from shorter.tasks import add_count
from shorter.utils import client


class RedirectView(APIView):
    queryset = Token.objects.all()

    def get_redirect_url(self, subpart):
        redirect_url = client.get(subpart)
        if redirect_url is None:
            instance = get_object_or_404(self.queryset, subpart=subpart)
            redirect_url = instance.full_url
            client.set(subpart, redirect_url)
        return redirect_url

    def get(self, request, subpart, *args, **kwargs):
        redirect_url = self.get_redirect_url(subpart)
        add_count.delay(subpart)
        return HttpResponseRedirect(redirect_url)
