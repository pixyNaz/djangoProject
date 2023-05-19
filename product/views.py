from django.shortcuts import render


from product.models import Product


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':

        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'product/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product
        }

        return render(request, 'product/detail.html', context=context)