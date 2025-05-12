from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment
from django.contrib.auth.decorators import login_required, permission_required
from .forms import AssignmentForm
from .forms import UserRegisterForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect('assignment_list')  # after signup, send to assignment list
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

# Add the root_redirect view here
@login_required
def root_redirect(request):
    return redirect('login')  # Redirect to the assignment list page

@login_required
def assignment_list(request):
    query = request.GET.get('q', '')
    if query:
        assignments = Assignment.objects.filter(name__icontains=query, assigned_to=request.user)
    else:
        assignments = Assignment.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/assignment_list.html', {'assignments': assignments})


@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, assigned_to=request.user)
    return render(request, 'tasks/assignment_detail.html', {'assignment': assignment})

@login_required
def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.save()
            assignment.assigned_to.set([request.user])  # Auto-assign to current user
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'tasks/assignment_form.html', {'form': form})


@login_required
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, assigned_to=request.user)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'tasks/assignment_form.html', {'form': form})

    
@login_required
def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, assigned_to=request.user)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')
    return render(request, 'tasks/assignment_confirm_delete.html', {'assignment': assignment})
