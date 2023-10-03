from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Redactor, Newspaper, Topic
from .forms import RedactorCreationForm, RedactorExperienceUpdateForm, NewspaperForm, RedactorUpdateDataForm


def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()
    start_time_str = request.session.get('start_time')

    if not start_time_str:
        start_time_str = timezone.now().isoformat()
        request.session['start_time'] = start_time_str

    start_time = timezone.datetime.fromisoformat(start_time_str)

    time_spent_seconds = (timezone.now() - start_time).seconds

    minutes, seconds = divmod(time_spent_seconds, 60)

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "time_spent_minutes": minutes,
        "time_spent_seconds": seconds,
    }

    return render(request, "bureau/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    paginate_by = 5


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("bureau:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("bureau:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("bureau:topic-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 10
    queryset = Newspaper.objects.all().select_related("topic").order_by('-published_year')


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("bureau:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("bureau:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("bureau:newspaper-list")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm


class RedactorExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorExperienceUpdateForm
    success_url = reverse_lazy("bureau:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("bureau:redactor-list")


@login_required
def toggle_assign_to_newspaper(request, pk):
    redactor = Redactor.objects.get(id=request.user.id)
    if (
            Newspaper.objects.get(id=pk) in redactor.newspapers.all()
    ):  # probably could check if newspaper exists
        redactor.newspapers.remove(pk)
    else:
        redactor.newspapers.add(pk)
    return HttpResponseRedirect(reverse_lazy("bureau:newspaper-detail", args=[pk]))


class RedactorUpdateDataView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    template_name = 'bureau/redactor_update_data.html'
    form_class = RedactorUpdateDataForm

    def get_success_url(self):
        return reverse_lazy("bureau:redactor-list")
