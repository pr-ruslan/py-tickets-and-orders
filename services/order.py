from datetime import datetime
from django.db import transaction
from django.db.models import QuerySet

from db.models import Order, Ticket, User, MovieSession


def create_order(tickets: list[dict],
                 username: str,
                 date: str = None) -> None:
    with transaction.atomic():
        new_order = Order.objects.create(user=User.objects.get(username=username))
        if date:
            new_order.date = datetime.strptime(date, "%Y-%m-%d %H:%M")
            print(new_order.date)
        new_order.save()
        print(new_order)

        for ticket in tickets:
            Ticket.objects.create(
                movie_session=MovieSession.objects.get(id=ticket['movie_session']),
                order=new_order,
                row=ticket["row"],
                seat=ticket["seat"]
            )
        return new_order

def get_orders(username = None) -> QuerySet:
    orders = Order.objects.all()
    if username:
        orders = orders.filter(user__username=username)
    return orders

