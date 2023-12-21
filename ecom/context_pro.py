from .models import catagory,Cart

def base_data(request):
    Cart_count = 0
    cat_data = catagory.objects.all()
    if request.user.is_authenticated :
        Cart_count= Cart.objects.filter(u_id=request.user).count()
        print(Cart_count)
    return {'cat_data':cat_data}






































































