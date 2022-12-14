from django.db.models import QuerySet

from core.models import Staff


def list_staff():
    return Staff.objects.all()