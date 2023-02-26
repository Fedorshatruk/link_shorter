from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import MiddlewareMixin

from shorter.models import Owner


class OwnerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, "session"):
            raise ImproperlyConfigured(
                "The Django owner middleware requires session "
                "middleware to be installed. Edit your MIDDLEWARE setting to "
                "insert "
                "'django.contrib.sessions.middleware.SessionMiddleware' before "
                "'shorter.middleware.owner.OwnerMiddleware'."
            )
        if session_key := request.session.session_key:
            request.owner, created = Owner.objects.get_or_create(session_id=session_key)
            del created
        else:
            request.session.save()
            request.owner = None
