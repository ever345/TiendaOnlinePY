from django.views import generic
from shipping_address.models import ShippingAddress

class ShippingAddressListView(generic.ListView):
    model = ShippingAddress
    template_name = 'hipping_addresses.html'
    
    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
