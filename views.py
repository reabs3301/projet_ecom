from django.shortcuts import render
from .models import product,client, acheter # Import the Product model
# Create your views here.

def home(request):
    products = product.objects.all()
    return render(request , 'home.html' , {'products' : products})

def details(request , prod_id , quantite):
    products = product.objects.get(id = prod_id)

    return render(request , 'details.html' , {'products' : products , 'quantite' : quantite})

def decrease(request , prod_id , client_id):
    products = product.objects.get(id = prod_id)

    if products.quantite > 0:  
        products.quantite -= 1
        products.save()
        client_buy = client.objects.get(id = client_id)
        
        buy = acheter.objects.filter(id_product=prod_id, id_client=client_id).first()

        if buy:
            buy.total_amount += products.price  # Increase total amount
        else:
            buy = acheter(id_product=prod_id, id_client=client_id, total_amount=products.price)

        buy.save()
    return render(request, 'details.html', {'products': products , 'total' : buy.total_amount})


def searching(request):

    if request.method == 'POST':
        to_search = request.POST['input_to_pass']
        if to_search[0] == ':':
            
            category_to_search = to_search[ 1 : to_search.find('/')]
            if len(to_search[to_search.find('/')+1 : ].strip()) == 0:
                returned_items = {'products_returned' : product.objects.filter(categorie = category_to_search) , 'searched' : to_search[to_search.find('/')+1 : ]}
            else:
                returned_items = {'products_returned' : product.objects.filter(categorie = category_to_search , name__contains = to_search[to_search.find('/')+1 : ]) , 'searched' : to_search[to_search.find('/')+1 : ]}
            return render(request , "search.html" , returned_items)
        elif to_search[0] != ':':
            returned_items = {'products_returned' : product.objects.filter(name__contains = to_search) , 'searched' : to_search}
            return render(request , "search.html" , returned_items)
    return render(request , "search.html" , {'msg' : "you must type something"})


