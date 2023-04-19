from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Stream
from .forms import StreamForm

from stream.forms import StreamForm
from students.models import Student
from .models import Stream

def stream_list(request):
    streams = Stream.objects.all()
    return render(request, 'stream/stream_list.html', {'streams': streams})


def stream_detail(request, pk):
    stream = get_object_or_404(Stream, pk=pk)
    return render(request, 'stream/stream_detail.html', {'stream': stream})

def stream_create(request):
    if request.method == 'POST':
        form = StreamForm(request.POST)
        if form.is_valid():
            stream = form.save()
            return redirect('stream_detail', pk=stream.pk)
    else:
        form = StreamForm()
    return render(request, 'stream/stream_form.html', {'form': form})

def stream_edit(request, pk):
    stream = get_object_or_404(Stream, pk=pk)
    if request.method == 'POST':
        form = StreamForm(request.POST, instance=stream)
        if form.is_valid():
            form.save()
            return redirect('stream_detail', pk=pk)
    else:
        form = StreamForm(instance=stream)
    return render(request, 'stream/stream_edit.html', {'form': form})


def assign_students(request, pk):
    stream = get_object_or_404(Stream, pk=pk)
    students = Student.objects.all()
    if request.method == 'POST':
        student_ids = request.POST.getlist('students')
        stream.students.set(student_ids)
        return redirect('stream_detail', pk=pk)
    return render(request, 'stream/assign_students.html', {'students': students, 'stream': stream})



# ========================================================

class StreamListView(ListView):
    model = Stream
    template_name = 'stream/stream_list.html'
    context_object_name = 'streams'

class StreamCreateView(CreateView):
    model = Stream
    form_class = StreamForm
    template_name = 'stream/stream_form.html'

class StreamUpdateView(UpdateView):
    model = Stream
    form_class = StreamForm
    template_name = 'stream/stream_form.html'

class StreamDeleteView(DeleteView):
    model = Stream
    template_name = 'stream/stream_confirm_delete.html'
    success_url = reverse_lazy('stream_list')

class StreamDetailView(ListView):
    model = Student
    template_name = 'stream/stream_detail.html'
    context_object_name = 'students'

    def get_queryset(self):
        self.stream = get_object_or_404(Stream, id=self.kwargs['pk'])
        return Student.objects.filter(stream=self.stream)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stream'] = self.stream
        return context

