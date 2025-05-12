from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Contact, Category, Client, Product, About, Carousel, Certificate


@require_GET
def ajax_search_products(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return JsonResponse([], safe=False)

    products = Product.objects.filter(Q(name_uz__icontains=query) | Q(name_ru__icontains=query))[:10]
    results = [{
        "id": p.id,
        "name": p.name,
        "image": p.image.url,
    } for p in products]

    return JsonResponse(results, safe=False)


def index(request):
    contract = Contact.objects.first()
    about = About.objects.first()
    categories = Category.objects.all()
    clients = Client.objects.all()
    carousel = Carousel.objects.all()
    products = Product.objects.all()[:8]
    return render(request, 'index.html',
                  {'contract': contract, 'categories': categories, 'clients': clients, 'about': about,
                   'carousel': carousel, 'products': products})


def about(request):
    about = About.objects.first()
    certificates = Certificate.objects.all()
    clients = Client.objects.all()
    categories = Category.objects.all()
    contract = Contact.objects.first()
    return render(request, 'about.html',
                  {'about': about, 'certificates': certificates, 'clients': clients, 'categories': categories,
                   'contract': contract})


def contact(request):
    contract = Contact.objects.first()
    categories = Category.objects.all()
    return render(request, 'contact.html', {'contract': contract, 'categories': categories})


def catalog(request):
    categories = Category.objects.all()
    contract = Contact.objects.first()
    return render(request, 'catalog.html', {'categories': categories, 'contract': contract})


def products_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    contract = Contact.objects.first()
    cat = request.GET.get('cat')
    if cat:
        products = products.filter(category_id=cat)
        category = Category.objects.get(pk=cat)
    return render(request, 'catalog-filter.html',
                  {'categories': categories, 'products': products, 'contract': contract, 'category': category})


def detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    contract = Contact.objects.first()
    categories = Category.objects.all()
    return render(request, 'product-inner.html',
                  {'product': product, 'categories': categories, 'contract': contract})
