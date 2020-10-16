import math
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404
from .forms import TransactionForm
from datetime import datetime
from movie.models import Movie
from transaction.models import Transaction
from customer.models import Customer

# Create your views here.

class TransactionIndexView(View):
    def get(self, request):
        customer = Customer.objects.all()
        movie = Movie.objects.all()
        transaction = Transaction.objects.all()
        return render(request, 'transaction/transaction_dashboard.html', {"trans":transaction, "mov":movie, "cust":customer})

    def post(self, request):
        if request.method == 'POST':
            if 'btnTransact' in request.POST:
                return redirect('transaction:transact')
            if 'btnDelete' in request.POST:
                trans_id = request.POST.get("trans_id")
                #Movie.objects.filter(id = customer_id).delete()
                trans = Transaction.objects.get(pk = trans_id)
                movies = trans.movie_id.all()

                for m in movies:
                    moov = Movie.objects.get(pk=m.id)
                    moov.no_of_items = moov.no_of_items + 1
                    moov.save()

                update = Transaction.objects.filter(id = trans_id).update(is_deleted=True)
                messages.success(request, 'Transaction info was deleted successfully!')

        return redirect('transaction:transaction_index')

class TransactionView(View):
    def get(self, request):
        customer = Customer.objects.all()
        movie = Movie.objects.all()

        return render(request, 'transaction/transaction.html', {"mov":movie, "cust":customer})

    def post(self, request):
        if request.method == "POST":
            form = TransactionForm(request.POST, request.FILES)
            data = request.POST
            
            if form.is_valid():
                default = 200
                date_of_transaction = data.get("date_of_transaction")
                room_no = data.get("room_no")
                cost = default 
                customer_id = data.get("customer_id")
                movie = data.get("movie_list")
                movie = movie.split(',')
                print(movie)
                for mov in movie:
                    m = Movie.objects.get(pk=mov)
                    m.no_of_items = m.no_of_items - 1
                    cost = cost + m.price
                    m.save()

                customer_id = Customer.objects.get(pk=customer_id)
                form = Transaction(date_of_transaction = date_of_transaction, room_no = room_no,
                            cost = cost, customer_id=customer_id)
                form.save()
                
                for mov in movie:
                    form.movie_id.add(mov)
                form.save() 

                messages.success(request, 'Transaction was successful!')
                return redirect('transaction:transaction_index')
            else:     
                messages.success(request, 'Sorry something went wrong!')
                return redirect('transaction:transact')
        else:
            messages.success(request, 'Sorry something went wrong!')
            return redirect('transaction:transact')
