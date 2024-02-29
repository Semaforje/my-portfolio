from django.views import generic
from .models import Project


# Create your views here.
class IndexView(generic.ListView):
    model = Project
    template_name = "portfolio/index.html"
    context_object_name = "project_list"


class DetailView(generic.DetailView):
    model = Project
    template_name = "portfolio/detail.html"



