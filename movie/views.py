import math
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404
from .forms import MovieForm
from datetime import datetime
from movie.models import Movie

# Create your views here.

class MovieIndexView(View):
    def get(self, request):
        data = Movie.objects.all()
        return render(request, 'movie/movie_dashboard.html', {'movie': data})

    def post(self, request):
        if request.method == 'POST':
            if 'btnDelete' in request.POST:
                movie_id = request.POST.get("mov_id")
                #Movie.objects.filter(id = customer_id).delete()
                update = Movie.objects.filter(id = movie_id).update(is_deleted=True)
                movie = Movie.objects.get(pk=movie_id)
                messages.success(request, '<b>' + movie.title + '</b> info was deleted successfully!')
            elif 'btnRegister' in request.POST:
                return redirect('movie:movie_registration')
            elif 'btnUpdate' in request.POST:
                form = MovieForm(request.POST, request.FILES)
                data = request.POST
                if form.is_valid():
                    movie_id = data.get("movie-id")
                    id_as_string = str(movie_id)
                    date_registered = data.get("date_registered")
                    sku = data.get("sku")
                    genre = ', '.join(data.getlist('genre'+id_as_string))
                    title = data.get("title")
                    release_date = data.get("release_date")
                    director = data.get("director")
                    casts = data.get("casts"+id_as_string)
                    price = data.get("price")
                    no_of_items = data.get("no_of_items")
                    image = request.FILES.get('cover_image', None)

                    if image is not None:
                        cover_image = image
                        movie = Movie.objects.get(pk=movie_id)
                        movie.image = cover_image
                        movie.save()
                        
                    Movie.objects.filter(id=movie_id).update(date_registered = date_registered, sku = sku,
                        genre = genre, title = title, release_date = release_date,
                        director = director, casts=casts, price = price, no_of_items = no_of_items)

                    messages.success(request, '<b>' +title + '</b> was updated successfully!')
                return redirect('movie:movie_view')
        return redirect('movie:movie_view')

class MovieRegistrationView(View):
    def get(self, request):
        return render(request, 'movie/movie_registration.html')
    
    def post(self, request):
        form = MovieForm(request.POST, request.FILES)	
        data = request.POST

        if form.is_valid():
            date_registered = data.get("date_registered")
            sku = data.get("sku")
            genre = ', '.join(data.getlist('genre'))
            title = data.get("title")
            release_date = data.get("release_date")
            director = data.get("director")
            casts = data.get("casts")
            price = data.get("price")
            no_of_items = data.get("no_of_items")
            image = request.FILES.get('cover_image', None)

            if image is not None:
                cover_image = image
                form = Movie(date_registered = date_registered, sku = sku,
                        genre = genre, title = title, release_date = release_date,
                        director = director, casts=casts, price = price, no_of_items = no_of_items,
                        image = cover_image)
            else:
                form = Movie(date_registered = date_registered, sku = sku,
                        genre = genre, title = title, release_date = release_date,
                        director = director, casts=casts, price = price, no_of_items = no_of_items)
            
            form.save()

            messages.success(request, '<b>' + title + '</b> was saved successfully!')
            return redirect('movie:movie_view')
        else:
            messages.success(request, 'There was an error during form submission')
            return redirect('movie:movie_registration')


