from django.shortcuts import render, redirect
from main_app.models import DishCategory, Dishes, Events, Gallery, Whyus, Chefs,Special, Reviews, BookTable,Contact, About
# Create your views here.

def manager_view(request):
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dishes.objects.filter(is_visible=True)
    events = Events.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    causes = Whyus.objects.all()
    chefs = Chefs.objects.all()
    special = Special.objects.filter(is_visible=True)
    reviews = Reviews.objects.all()
    about = About.objects.all()
    return render(request, 'manager_page.html', context={
        'categories': categories,
        'events': events,
        'gallery': gallery,
        'causes':causes,
        'chefs': chefs,
        'special': special,
        'reviews': reviews,
        'about': about
    })

def manager_booked_view(request):
    booked = BookTable.objects.filter(is_processed=False)
    return render(request, 'message_delet.html', context={'booked': booked})

def update_booked_view(request, pk):
    BookTable.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:booked')

def manager_message(request):
    message = Contact.objects.filter(is_proccesed=False)
    return render(request, 'message.html', context={'message': message})

def manager_message_update(request,pk):
     Contact.objects.filter(pk=pk).update(is_proccesed=True)
     return redirect('manager2:message')