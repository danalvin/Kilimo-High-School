from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Stream
from .forms import StreamForm
from django.views import View
from stream.forms import StreamForm
from students.models import Student
from .models import Stream
from django.contrib.auth.mixins import LoginRequiredMixin



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



class AddStudentToStreamView(LoginRequiredMixin, View):
    def get(self, request, pk):
        stream = get_object_or_404(Stream, pk=pk)
        students = stream.students.all()
        available_students = Student.objects.exclude(pk__in=students)
        context = {
            'stream': stream,
            'students': students,
            'available_students': available_students,
        }
        return render(request, 'stream/add_student_to_stream.html', context)

    def post(self, request, pk):
        stream = get_object_or_404(Stream, pk=pk)
        student_pk = request.POST.get('student')
        if student_pk:
            student = get_object_or_404(Student, pk=student_pk)
            stream.students.add(student)
            messages.success(request, f'{student.name} added to {stream.name} stream.')
        else:
            messages.warning(request, 'Please select a student to add.')
        return redirect(reverse('stream:add_student_to_stream', args=[pk]))
    
# ========================================================

class StreamListView(ListView):
    model = Stream
    template_name = 'stream/stream_list.html'
    context_object_name = 'streams'

class StreamCreateView(CreateView):
    model = Stream
    form_class = StreamForm
    template_name = 'stream/stream_form.html'
    success_url = reverse_lazy('stream_list')


class StreamUpdateView(UpdateView):
    model = Stream
    form_class = StreamForm
    template_name = 'stream/stream_form.html'
    success_url = reverse_lazy('stream_list')


class StreamDeleteView(DeleteView):
    model = Stream
    template_name = 'stream/stream_confirm_delete.html'
    success_url = reverse_lazy('stream_list')

class StreamDetailView(ListView):
    model = Student
    template_name = 'stream/stream_detail.html'
    context_object_name = 'students'

    def get_queryset(self):
        self.stream = get_object_or_404(Stream, slug=self.kwargs['slug'])
        return Student.objects.filter(stream=self.stream)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streams'] = self.stream
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        unassigned_students = queryset.filter(stream=None)
        for student in unassigned_students:
            print(student.stream)
        return unassigned_students