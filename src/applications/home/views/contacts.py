from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = "home/contactPage.html"
