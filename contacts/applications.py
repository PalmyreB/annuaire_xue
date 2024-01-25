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
        viewsets.RecommendedContactWithFieldFilterViewset(),
        # Add a viewset per field of competence
        # TODO: Fix the bug caused by next lines.
        #  It seems that applications are initialized before models.
        #  Hence, it is not possible to refer to objects of a model at initialization.
        #  However, uncommenting these lines when the application is running works.
        # *[
        #     viewsets.RecommendedContactByFieldViewset(title=str(field), field=field)
        #     for field in models.FieldOfCompetence.objects.all()
        # ],
    ]
