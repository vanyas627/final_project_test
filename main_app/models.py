from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class DishCategory(models.Model):
    title = models.CharField(max_length=50, blank=False)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    class Meta:
        ordering = ('position',)
        verbose_name_plural = "Категорії"

    def __str__(self):
        return f'{self.title}'

class Dishes(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False)
    position = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=100, unique=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(DishCategory, related_name='dishes', on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='dishes')
    discount = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('position', )
        verbose_name_plural = "Страви"

    def total_price(self):
        return self.price - self.price * (self.discount / 100)

    def __str__(self):
        return f'{self.title}'


class Special(models.Model):
    title = models.CharField(max_length=50, blank=False)
    position = models.PositiveSmallIntegerField()
    desk = models.TextField(max_length=1000, blank=True)
    ingredients = models.CharField(max_length=100, blank=False)
    photo = models.ImageField(upload_to='dishes')
    is_visible = models.BooleanField(default=True)


    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Спеціальні страви'

    def __str__(self):
        return f'{self.title}'


class Events(models.Model):

    title = models.CharField(max_length=100, blank=False)
    price = models.PositiveSmallIntegerField()
    desc = models.TextField(max_length=1000, blank=False)
    desc_caus_1 = models.TextField(max_length=1000, blank= True)
    desc_caus_2 = models.TextField(max_length=1000, blank=True)
    desc_caus_3 = models.TextField(max_length=1000, blank=True)
    desc_caus_4 = models.TextField(max_length=1000, blank=True)
    last_desc = models.TextField(max_length=1000, blank=False, default=None)
    photo = models.ImageField(upload_to='events')
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Події'

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery')
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position', )
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return f'{self.position}'

class Chefs(models.Model):
    name = models.CharField(blank=False, max_length=50)
    profession = models.CharField(blank=True, max_length=50)
    photo = models.ImageField(upload_to='chefs')
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Шефи'

    def __str__(self):
        return f'{self.name}'

class Reviews(models.Model):
    name = models.CharField(blank=False, max_length=50)
    profession = models.CharField(blank=True, max_length=50)
    photo = models.ImageField(upload_to='reviews', blank=True)
    desc = models.TextField(max_length=2000, blank=False)

    class Meta:
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f'{self.name}'

class Whyus(models.Model):

    NUMBERS = (
        (1, '1' ),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )


    title = models.CharField(blank=False, max_length=100)
    desc = models.TextField(max_length=1000, blank=False)
    position = models.IntegerField(default=0, choices=NUMBERS)

    class Meta:
        ordering = ('position', )
        verbose_name_plural = 'Why choose our restaurant'

    def __str__(self):
        return f'{self.title}'


class About(models.Model):
    title = models.CharField(blank=False, max_length=200)
    desc = models.TextField(max_length=1000, blank=True)
    desc_caus_1 = models.TextField(max_length=1000, blank= True)
    desc_caus_2 = models.TextField(max_length=1000, blank=True)
    desc_caus_3 = models.TextField(max_length=1000, blank=True)
    last_desc = models.TextField(max_length=2000, blank=False)
    photo = models.ImageField(upload_to='about')


    class Meta:
        verbose_name_plural = 'Про ресторан'

    def __str__(self):
        return f'{self.title}'

class BookTable(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_validator = RegexValidator(regex=r'^\+?3?8?0?\d{2}[- ]?(\d[ -]?){7}$',
                                     message='Phone number is waited n format 380xx xxx xx xx')
    phone = models.CharField(max_length=20, validators=(phone_validator,))
    date = models.DateField()
    time = models.TimeField()
    date_response = models.DateTimeField(auto_now=True)
    data_request = models.DateTimeField(auto_now_add=True)
    people = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=500, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data_request',)
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'{self.name}'

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(max_length=2000, blank=False)
    is_proccesed = models.BooleanField(default=False)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Повідомлення'

    def __str__(self):
        return f'{self.name}'