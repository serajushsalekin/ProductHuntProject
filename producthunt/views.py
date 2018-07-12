from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Product, User
from django.utils import timezone


def home(request):
    products = Product.objects.all()
    return render(request, 'producthunt/home.html', {'products': products})


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon']\
                and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.now()
            product.user = request.user
            product.save()
            # return redirect('home')
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'producthunt/create.html', {'error': "All fields are required"})

    else:
        return render(request, 'producthunt/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk= product_id)
    return render(request, 'producthunt/detail.html', {'product': product})


@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        if product.votes_total is True:
            return HttpResponseRedirect("Already liked")
        else:
            product.votes_total += True
            product.save()
        return redirect('/products/' + str(product.id))

"""
@login_required
def upvote(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if Product.objects.filter(id=product.pk, user_id=request.user.id).exists():
        return HttpResponseRedirect('"Sorry, but you have already voted.')
    else:
        p = get_object_or_404(Product, pk=product_id)
        p.votes_total+1
        p.save()
        #Product.objects.create(id=product_id, user_id=request.user.id)

        return redirect('/products/' + str(product.id))
    """