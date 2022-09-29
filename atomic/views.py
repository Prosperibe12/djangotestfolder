import decimal

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import transaction

from .forms import Payment
from .models import customer


# Create your views here.
# @transaction.atomic
def index_view(request):
    form = Payment
    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            x = form.cleaned_data.get('payor')
            y = form.cleaned_data.get('payee')
            a = decimal.Decimal(form.cleaned_data.get('amount'))

            sender = customer.objects.select_for_update().get(name=x)
            receiver = customer.objects.select_for_update().get(name=y)
            # atomicity within the context manager
            with transaction.atomic():
                sender.balance -= a
                sender.save()

                receiver.balance += a
                receiver.save()
                return HttpResponseRedirect('/')
    context = {
        'Title': 'Home Page',
        'form': form
    }
    return render(request, 'atomic/index.html', context)
