from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404

from .models import Product, Comment
from .forms import CommentForm

class ProductListView(ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
    #    product = self.get_object()
       context['comment_form'] = CommentForm() 
    #    context['comments_active_manager'] = Comment.comments_active_manager.filter(product=product)
       return context

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        
        return super().form_valid(form)
