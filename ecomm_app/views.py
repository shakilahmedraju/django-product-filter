from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category, Brand, Warranty, Seller







def category_page(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        
        selected_brands = request.GET.getlist('brand[]')
        selected_warranties = request.GET.getlist('warranty[]')
        selected_sellers = request.GET.getlist('seller[]')

        min_price = request.GET.get('min_price')  
        max_price = request.GET.get('max_price')

        sort_by = request.GET.get('sort_by')  

        products = Product.objects.all()
        
        if selected_brands:
            products = products.filter(brand__in=selected_brands)
        if selected_warranties:
            products = products.filter(warranty__in=selected_warranties)
        if selected_sellers:
            products = products.filter(seller__in=selected_sellers)

        # Price filtering
        if min_price and max_price:
            products = products.filter(discounted_price__range=(min_price, max_price))

        if sort_by == '2':
            products = products.order_by('name')
        elif sort_by == '3':
            products = products.order_by('-price')
        elif sort_by == '4':
            products = products.order_by('price')

        data = {
            'products': list(products.values())
        }
        return JsonResponse(data)
    
    
    categories = Category.objects.all()
    category_name = None
    product_count = 0
    brands = Brand.objects.all()
    warranties = Warranty.objects.all()
    sellers = Seller.objects.all()

    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.objects.filter(category = categoryID).order_by('-id')
        category_name = Category.objects.get(id=categoryID)
        product_count = Product.objects.filter(category=category_name).count()
        
    else:
        products = Product.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
        'warranties': warranties,
        'sellers': sellers,
        'products': products,
        'category_name': category_name,
        'product_count': product_count,
    }

    return render(request, 'category.html', context)


