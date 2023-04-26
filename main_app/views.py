from django.shortcuts import render, redirect
from .models import DishCategory, Dishes, Events, Gallery, Whyus, Chefs,Special, Reviews, About
from .forms import BookTableForm, ContactForm


def main_view(request):
    if request.method == 'POST':
        form_book = BookTableForm(request.POST)
        contact_form = ContactForm(request.POST)
        if form_book.is_valid():
            form_book.save()
            return redirect('/')
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/')

    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dishes.objects.filter(is_visible=True)
    events = Events.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    causes = Whyus.objects.all()
    chefs = Chefs.objects.all()
    special = Special.objects.filter(is_visible=True)
    reviews = Reviews.objects.all()
    forms = BookTableForm()
    message = ContactForm()
    about = About.objects.all()
    return render(request, 'main_page.html', context={
        'categories': categories,
        'events': events,
        'gallery': gallery,
        'causes':causes,
        'chefs': chefs,
        'special': special,
        'reviews': reviews,
        'forms':forms,
        'message': message,
        'about': about
    })




