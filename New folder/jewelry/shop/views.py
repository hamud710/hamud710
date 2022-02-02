from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProductFilter
from main.models import *
from django.db.models import Count, Q

def shop(request):
    about = AboutUs.objects.order_by("?").first()
    shop = Item.objects.all()
    cat = JewelleryCategory.objects.all()
    Item_list = Item.objects.all()
    

    f = ProductFilter(request.GET, queryset=shop)
    Item_list = f.qs
    paginator = Paginator(Item_list, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    


    

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    
    
    context = {
        'shop': shop,
        'about': about,
        'cat':cat,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'filter': f,
        
    }

    return render(request, 'shop-list.html',context)


def search(request):
    about = AboutUs.objects.order_by("?").first()
    shop = Item.objects.all()
    cat = JewelleryCategory.objects.all()
    Item_list = Item.objects.all()
    query = request.GET.get('q')
    if query:
        Item_list = Item_list.filter(
            Q(Name__icontains=query) |
            Q(about__icontains=query)
        ).distinct()

    f = ProductFilter(request.GET, queryset=Item_list)
    Item_list = f.qs
    paginator = Paginator(Item_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    


    

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    
    
    context = {
        'shop': shop,
        'about': about,
        'cat':cat,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'filter': f
    }

    return render(request, 'shop-list.html',context)




def Catshop(request,id):
    shop = Item.objects.all()
    cat = JewelleryCategory.objects.all()
    Item_list = Item.objects.filter(Category=id)

    f = ProductFilter(request.GET, queryset=shop)
    Item_list = f.qs
    paginator = Paginator(Item_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'shop': shop,
        'cat':cat,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'filter': f
    }
    return render(request, 'shop-list.html',context)
def details(request):
    shop = Item.objects.first()
    cat = JewelleryCategory.objects.all()
    context = {
        'shop': shop,
        'cat':cat,
    }
    return render(request, 'product-details.html',context)

def cart(request):
    val = request.POST.get('patient_id')
    Cart.objects.create(Name= Item.objects.filter(pk=val).first() )
    about = AboutUs.objects.order_by("?").first()
    shop = Cart.objects.all()
    cat = JewelleryCategory.objects.all()
    Item_list = Cart.objects.all()
    
    
    total = 0
    for pr in Item_list:
        pricefor = pr.Name.Price * pr.Quantity
        total = total + pricefor
    

    
    paginator = Paginator(Item_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    


    

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    
    
    context = {
        'val':val,
        'shop': shop,
        'about': about,
        'cat':cat,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'total':total,
        
    }

    return render(request, 'cart.html',context)

