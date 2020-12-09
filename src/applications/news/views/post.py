from django.views.generic import DetailView

from applications.news.models import Articles


class PostView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'post'
