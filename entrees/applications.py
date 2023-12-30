from django.contrib.auth import get_user_model
from viewflow.urls import Application
from viewflow.urls import ModelViewset

from . import models, viewsets

User = get_user_model()


class HomeApplication(Application):
    base_template_name = "viewflow/base_page.html"
    menu_template_name = None
    title = "Accueil"
    icon = "home"
    app_name = "home"
    viewsets = [viewsets.HomeViewset()]


class PeopleApplication(Application):
    title = "Utilisateurs et contacts"
    icon = "people"
    app_name = "people"
    viewsets = [
        viewsets.RecommendedContactAddedByUserViewset(),
        viewsets.RecommendedContactReadOnlyViewset(),
        viewsets.ReferentContactViewset(),
        ModelViewset(model=User),
    ]


class FieldsApplication(Application):
    title = "Domaines de compétence"
    icon = "book"
    app_name = "fields"
    viewsets = [
        # ReadonlyModelViewset(model=models.FieldOfCompetence, icon="book"),
        # Add a viewset per field of competence
        viewsets.RecommendedContactWithFieldFilterViewset(),
        *[
            viewsets.RecommendedContactByFieldViewset(title=str(field), field=field)
            for field in models.FieldOfCompetence.objects.all()
        ],
    ]
