from django.db import transaction

from db.models import Ticket


def create_order(tickets: list[dict],
                 username: str,
                 date: str = None):
    with transaction.atomic():
        pass