
from django.shortcuts import render
from django.db.models import Q
from django.views import generic


from products.models import Products

class ProductListview(generic.ListView):
    template_name = 'index.html'
    queryset = Products.objects.all().order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        context['products'] = context['object_list']
        return context
    
class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'product.html'
    
class ProductSearchView(generic.ListView):
    template_name = 'search.html'
    
    def get_queryset(self):
        filter = Q(title__icontains=self.query()) | Q(Category__title__icontains=self.query())
        return Products.objects.filter(title__icontains=self.query())
    
    def query(self):
        
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['products_list'].count()  
        return context


