from .serializers import IndianPincodeSerializer
from .models import IndianPincode
from rest_framework import generics


class PinCodeList(generics.ListAPIView):
    serializer_class = IndianPincodeSerializer

    def get_queryset(self):
        pincode = self.request.query_params.get('pincode', None)
        if pincode is not None:
            return IndianPincode.objects.filter(pin_code=pincode)


class PONameList(generics.ListAPIView):
    serializer_class = IndianPincodeSerializer

    def get_queryset(self):
        po_name = self.request.query_params.get('po_name', None)
        if po_name is not None:
            return IndianPincode.objects.filter(office_name__icontains=po_name)
