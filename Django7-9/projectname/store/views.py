from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookingForm, MusicianForm
# # Create your views here.


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Completed")
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Completed")
            # return redirect('musician')
    form = MusicianForm()
    dict_form={
        'form': form
    }
    return render(request, 'musician.html' , dict_form)
           

from .models import *
def departments(request):
    dept_dict={
        'dept': Departments.objects.all()
    }
    return  render(request, 'departments.html', dept_dict)

def doctors(request):
    dict_docs = {
        'doc': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)


def about1(request):
    return render(request, 'about.html')

def base1(request):
    return render(request, 'base.html')
def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

# def booking(request):
#     return render(request, 'booking.html')


from django.views.generic import ListView
class Tasklistview(ListView):
    model = Departments
    template_name = 'cls_department.html'
    context_object_name = 'dept'


from django.views.generic.detail import DetailView
class TaskDetailtview(DetailView):
    model = Departments
    template_name = 'dep_clsdetail.html'
    context_object_name = 'depts'

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
class TaskDeleteView(DeleteView):
    model = Departments
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    
from django.views.generic.edit import CreateView  
class EmployeeCreate(CreateView):  
    model = Departments
    template_name = 'cls_create.html' 
    fields = '__all__' 
    success_url = reverse_lazy('home')

    # def get_success_url(self):
    #     return reverse_lazy('cbdetail', kwargs = {'pk':self.object.id})


from django.views.generic.edit import  UpdateView

class TaskUpdateView(UpdateView):
    model = Departments
    template_name = 'cls_update.html'
    # context_object_name = 'dept'
    fields = ('dep_name','dep_description')

    def get_success_url(self):
        return reverse_lazy('cbdetail', kwargs = {'pk':self.object.id})
    

    
from django.shortcuts import render, get_object_or_404
from .models import Departments

def task_detail_view(request, pk):
    department = get_object_or_404(Departments, pk=pk)
    context = {
        'depts': department,
    }
    return render(request, 'dep_clsdetail.html', context)
