from django.urls import path
from applications.home.apps import HomeConfig
from applications.home.views import IndexView
from applications.home.views import CorrectionView
from applications.home.views import MassageView
from applications.home.views import TeipirovanieView
from applications.home.views import StrokeView
from applications.home.views import ContactsView

app_name = HomeConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("zvuk/", CorrectionView.as_view(), name="zvuk"),
    path("mas/", MassageView.as_view(), name='mas'),
    path("teip/", TeipirovanieView.as_view(), name='teip'),
    path("insult/", StrokeView.as_view(), name='insult'),
    path("contacts/", ContactsView.as_view(), name='contacts'),
]

