from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment
from django.contrib.auth.decorators import login_required, permission_required
from .forms import AssignmentForm

# Add the root_redirect view here
@login_required
def root_redirect(request):
    return redirect('assignment_list')  # Redirect to the assignment list page

@login_required
def assignment_list(request):
    query = request.GET.get('q', '')
    if query:
        assignments = Assignment.objects.filter(name__icontains=query)
    else:
        assignments = Assignment.objects.all()
    return render(request, 'tasks/assignment_list.html', {'assignments': assignments})

@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    return render(request, 'tasks/assignment_detail.html', {'assignment': assignment})

@permission_required('tasks.add_assignment')
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'tasks/assignment_form.html', {'form': form})

@permission_required('tasks.change_assignment')
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')  # Redirect to the list after saving
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'tasks/assignment_form.html', {'form': form})
    
@permission_required('tasks.delete_assignment')
def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        # Perform the deletion only for POST requests
        assignment.delete()
        return redirect('assignment_list')  # Redirect to the list after deletion
    # Render the confirmation page for GET requests
    return render(request, 'tasks/assignment_confirm_delete.html', {'assignment': assignment})