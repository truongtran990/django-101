from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import ContactForm
from django.shortcuts import render

from user.models import Publisher, Book

class MyView(View):
    def get(self, request):
        print("at here")
        return HttpResponse('result')


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'
    template_name = 'books/publisher_list.html'
    
    def get_queryset(self):
        print("PublisherListView")
        return super().get_queryset()


class PublisherDetailView(DetailView):
    model = Publisher
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["book_list"] = Book.objects.all()
        return context
    
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            print("[INFO] form", form)
            return JsonResponse({'success': True})
        else:
            print("[ERROR] form error", form)
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    
    return render(request, 'contacts/contact.html', {'form': form})