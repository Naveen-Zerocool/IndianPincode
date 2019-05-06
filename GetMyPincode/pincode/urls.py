from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^location/lookup/pincode$', PinCodeList.as_view()),
    url(r'^location/lookup/po_name$', PONameList.as_view()),
]
