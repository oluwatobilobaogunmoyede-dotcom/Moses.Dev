from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Project

def home(request):
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)
    if not featured_projects.exists():
        featured_projects = projects[:3]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! Your message has been sent successfully."
            )
            return redirect("home")
    else:
        form = ContactForm()

    context = {
        "projects": projects,
        "featured_projects": featured_projects,
        "form": form,
    }
    return render(request, "projects/home.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "projects/project_detail.html", {"project": project})
