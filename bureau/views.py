from django.shortcuts import render
from django.utils import timezone

from bureau.models import Redactor, Topic


def index(request):
    num_redactors = Redactor.objects.count()
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
        "num_topics": num_topics,
        "time_spent_minutes": minutes,
        "time_spent_seconds": seconds,
    }

    return render(request, 'bureau/index.html', context=context)
