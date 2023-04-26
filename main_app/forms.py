from django import forms
from .models import BookTable, Contact

class BookTableForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control",
                                                                        "id": "name",
                                                                        "placeholder": "Your Name",
                                                                        "data-rule": "minlen:4",
                                                                        "data-msg": "Please enter at least 4 chars"
                                                                        }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control",
                                                           "id": "email",
                                                           "placeholder":"Your Email",
                                                           "data-rule": "email",
                                                           "data-msg": "Please enter a valid email"
                                                           }))


    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control",
                                                                         "id":"phone",
                                                                         "placeholder": "Your Phone",
                                                                         "data-rule": "minlen:4",
                                                                         "data-msg": "Please enter at least 4 chars"
                                                                         }))

    date = forms.DateField(input_formats=['%Y-%m-%d', # 2006-10-23
                                          '%d-%m-%Y',
                                          '%d.%m.%Y',
                                          '%Y.%m.%d',
                                          '%d/%m/%Y',
                                          '%Y/%m/%d',
                                                        ],widget=forms.TextInput(attrs={"class": "form-control",
                                                         "id": "date",
                                                         "placeholder": "Date",
                                                         "data-rule": "minlen:4",
                                                         "data-msg": "Please enter at least 4 chars"
                                                         }))


    time = forms.TimeField(widget=forms.TextInput(attrs={"class": "form-control",
                                                         "id": "time",
                                                         "placeholder": "Time",
                                                         "data-rule": "minlen:4",
                                                         "data-msg": "Please enter at least 4 chars"
                                                         }))


    people = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control",
                                                                "id": "people",
                                                                "placeholder": "# of people",
                                                                "data-rule": "minlen:1",
                                                                "data-msg": "Please enter at least 1 chars"
                                                                }))

    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"class": "form-control",
                                                                           "rows": "5",
                                                                           "placeholder": "Message"
                                                                           }))


    class Meta:
        model = BookTable
        fields = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')



class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type":"text",
                                                                        "name":"name",
                                                                        "class": "form-control",
                                                                        "id":"name",
                                                                        "placeholder":"Your Name"
                                                                        }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"type":"email",
                                                            "class":"form-control",
                                                            "name": "email",
                                                            "id": "email",
                                                            "placeholder": "Your Email"
                                                            }))

    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type":"text",
                                                                           "class":"form-control",
                                                                           "name": "subject",
                                                                           "id": "subject",
                                                                           "placeholder":"Subject"
                                                                           }))

    message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={"class":"form-control",
                                                                            "name":"message",
                                                                            "rows":"8",
                                                                            "placeholder":"Message"
                                                                            }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

