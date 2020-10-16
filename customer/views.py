import math
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404
from .forms import CustomerForm
from .models import *

# Create your views here.
class CustomerIndexView(View):
    def get(self, request):
        data = Customer.objects.all()
        return render(request, 'customer/customer_dashboard.html', {'customer': data})
    
    def post(self, request):
        if request.method == 'POST':
            if 'btnDelete' in request.POST:
                customer_id = request.POST.get("cust_id")
                #Customer.objects.filter(person_ptr_id = customer_id).delete()
                #Person.objects.filter(id = customer_id).delete()
                update = Customer.objects.filter(person_ptr_id = customer_id).update(is_deleted=True)
                customer = Customer.objects.get(pk=customer_id)
                messages.success(request, '<b>' + customer.first_name + ' ' + customer.last_name + '\'s</b> info was deleted successfully!')
            elif 'btnRegister' in request.POST:
                return redirect('customer:customer_registration')
            elif 'btnUpdate' in request.POST:
                form = CustomerForm(request.POST, request.FILES)
                data = request.POST
                if form.is_valid():
                    customer_id = data.get("customer-id")
                    fname = data.get("first_name")
                    mname = data.get("middle_name")
                    lname = data.get("last_name")
                    street = data.get("street")
                    brgy = data.get("barangay")
                    province = data.get("province")
                    city = data.get("city")
                    state = data.get("state")
                    zip_code = data.get("zip")
                    birth_date = data.get("birth_date")
                    status = data.get("status")
                    gender = data.get("gender")
                    s_name = data.get("spouse_name")
                    s_occupation = data.get("spouse_occupation")
                    n_children = data.get("no_of_children")
                    image = request.FILES.get('profile_picture', None)

                    if image is not None:
                        profile_picture = image
                        customer = Customer.objects.get(pk=customer_id)
                        customer.profile_picture = profile_picture
                        customer.save()
                        
                    Customer.objects.filter(person_ptr_id = customer_id).update(first_name=fname, middle_name=mname, last_name=lname, 
                        street=street, barangay=brgy, province=province, city=city, state=state, zip_code=zip_code,
                        birth_date=birth_date, gender=gender, status=status,
                        spouse_name=s_name, spouse_occupation=s_occupation, no_of_children=n_children)

                    messages.success(request, '<b>' + fname + ' ' + lname + '\'s</b> info was updated successfully!')
                return redirect('customer:customer_index')
        return redirect('customer:customer_index')
    
class CustomerRegistrationView(View):
    def get(self, request):
        return render(request, 'customer/customer_registration.html')
    
    def post(self, request):
        form = CustomerForm(request.POST, request.FILES)
        data = request.POST

        if form.is_valid():
            date_registered = data.get("date_registered")
            fname = data.get("first_name")
            mname = data.get("middle_name")
            lname = data.get("last_name")
            street = data.get("street")
            brgy = data.get("barangay")
            province = data.get("province")
            city = data.get("city")
            state = data.get("state")
            zip_code = data.get("zip")
            birth_date = data.get("birth_date")
            status = data.get("status")
            gender = data.get("gender")
            s_name = data.get("spouse_name")
            s_occupation = data.get("spouse_occupation")
            n_children = data.get("no_of_children")
            image = request.FILES.get('profile_picture', None)

            if image is not None:
                profile_picture = image
                form = Customer(date_registered=date_registered,
                           first_name=fname, middle_name=mname, last_name=lname, 
                           street=street, barangay=brgy, province=province, city=city, state=state, zip_code=zip_code,
                           birth_date=birth_date, gender=gender, status=status,
                           spouse_name=s_name, spouse_occupation=s_occupation, no_of_children=n_children,
                           profile_picture=profile_picture, is_deleted=False
                           )
            else:
                form = Customer(date_registered=date_registered,
                           first_name=fname, middle_name=mname, last_name=lname, 
                           street=street, barangay=brgy, province=province, city=city, state=state, zip_code=zip_code,
                           birth_date=birth_date, gender=gender, status=status,
                           spouse_name=s_name, spouse_occupation=s_occupation, no_of_children=n_children,
                           is_deleted=False
                           )
            form.save()

            messages.success(request, '<b>' + fname + ' ' + lname + '</b> was registered successfully!')
            return redirect('customer:customer_index')
        else:
            messages.success(request, 'There was an error during form submission')
            return redirect('customer:customer_registration')