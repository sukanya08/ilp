from django.conf.urls import url, include
from boundary.views import Admin1sBoundary

state_patterns = [
    url(r'^boundary/admin1s$', Admin1sBoundary.as_view(), name='admin1s-boundary'),
    url(r'^boundary/admin2s$',Admin1sBoundary.as_view(), name='admin2s-boundary'),
    url(r'^boundary/admin3s$',Admin1sBoundary.as_view(), name='admin3s-boundary')
]

urlpatterns = [
    url(r'^(?P<state>[a-zA-z]{2})/', include(state_patterns))
]

