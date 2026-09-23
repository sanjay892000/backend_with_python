from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import DepartmentForm
from .models import Department


def department_list(request):

    search = request.GET.get("search", "")

    departments = Department.objects.all()

    if search:

        departments = departments.filter(

            Q(name__icontains=search) |
            Q(code__icontains=search)

        )

    paginator = Paginator(departments, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {

        "page_obj": page_obj,

        "search": search,

    }

    return render(
        request,
        "departments/list.html",
        context,
    )


def department_create(request):

    form = DepartmentForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Department created successfully."
        )

        return redirect("department_list")

    return render(
        request,
        "departments/create.html",
        {
            "form": form
        }
    )


def department_update(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk,
    )

    form = DepartmentForm(
        request.POST or None,
        instance=department,
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Department updated successfully."
        )

        return redirect("department_list")

    return render(
        request,
        "departments/update.html",
        {
            "form": form,
            "department": department,
        },
    )


def department_delete(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk,
    )

    if request.method == "POST":

        department.delete()

        messages.success(
            request,
            "Department deleted successfully."
        )

        return redirect("department_list")

    return render(
        request,
        "departments/delete.html",
        {
            "department": department,
        },
    )