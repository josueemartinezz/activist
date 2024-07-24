"""
Testing for the events app.
"""

import pytest
from django.urls import reverse
from tests.throttle import BaseTestThrottle

from django.test import Client
from faker import Faker
from .models import Event

from .factories import (
    EventFactory,
    EventAttendeeFactory,
    EventFormatFactory,
    EventAttendeeStatusFactory,
    EventResourceFactory,
    FormatFactory,
    RoleFactory,
)


class EventsThrottleTest(BaseTestThrottle):
    __test__ = True
    url = reverse("events:event-list")


def test_str_methods() -> None:
    event = EventFactory.build()
    event_attendee = EventAttendeeFactory.build()
    event_format = EventFormatFactory.build()
    event_attendee_status = EventAttendeeStatusFactory.build()
    event_resource = EventResourceFactory.build()
    _format = FormatFactory.build()
    role = RoleFactory.build()
    assert str(event) == event.name
    assert (
        str(event_attendee) == f"{event_attendee.user_id} - {event_attendee.event_id}"
    )
    assert str(event_format) == f"{event_format.id}"
    assert str(event_attendee_status) == event_attendee_status.status_name
    assert str(event_resource) == f"{event_resource.id}"
    assert str(_format) == _format.name
    assert str(role) == role.name


# @pytest.mark.django_db
# def test_events(client: Client) -> None:
#     """
#     Test the signup function.

#     Scenarios:
#     1. User successfully creates their event
#     2. User successfully updates their event
#     3. User attempts to update an event that isn't theirs
#     4. User attempts to delete an event that isn't theirs
#     5. User successfully deletes their own event
#     """
#     # Setup: Event Creation
#     fake = Faker()
#     event_name = fake.name()
#     event_tagline = fake.sentence()
#     event_type = fake.word()
#     event_description = fake.paragraph(nb_sentences=5)
#     event_get_involved_text = fake.paragraph(nb_sentences=5)

#     # Setup: User Creation
#     username_one = fake.name()
#     username_two = fake.name()
#     strong_password = fake.password(
#         length=12, special_chars=True, digits=True, upper_case=True
#     )
#     email_one = fake.email()
#     email_two = fake.email()

#     # Setup: User 1 Creation
#     response = client.post(
#         path="/v1/auth/signup/",
#         data={
#             "username": username_one,
#             "password": strong_password,
#             "password_confirmed": strong_password,
#             "email": email_one,
#         },
#     )

#     assert response.status_code == 201
#     assert UserModel.objects.filter(username=username_one).exists()


#     # Setup: User 2 Creation
#     response = client.post(
#         path="/v1/auth/signup/",
#         data={
#             "username": username_two,
#             "password": strong_password,
#             "password_confirmed": strong_password,
#             "email": email_two,
#         },
#     )

#     assert response.status_code == 201
#     assert UserModel.objects.filter(username=username_two).exists()


#     # 1. User successfully creates their event
#     response = client.post(
#         path="/v1/events/events/",
#         data={
#             "name": event_name,
#             "tagline": "Test tagline",
#             "created_by": username_one,
#             "type": "Test type",
#             "description": "Test description",
#             "get_involved_text": "Test get involved",
#         },
#     )

#     assert response.status_code == 201
#     assert Event.objects.filter(name=event_name).exists()
#     assert Event.objects.get(name=event_name).created_by == username_one


#     # 2. User successfully updates their event
#     event = Event.objects.get(name=event_name)
#     new_event_name = "Updated Event Name"
#     response = client.patch(
#         f"/v1/events/events/{event.id}/",
#         data={"name": new_event_name, "created_by": username_one},
#         content_type='application/json'
#     )

#     assert response.status_code == 200
#     assert Event.objects.filter(name=new_event_name).exists()


#     # 3. User attempts to update an event that isn't theirs
#     invalid_event_name = "Event Name that won't be inserted"
#     response = client.patch(
#         f"/v1/events/events/{event.id}/",
#         data={"name": invalid_event_name, "created_by": username_two},
#         content_type='application/json'
#     )

#     assert response.status_code == 401
#     assert not Event.objects.filter(name=invalid_event_name).exists()


#     # 4. User attempts to delete an event that isn't theirs
#     response = client.delete(
#        f"/v1/events/events/{event.id}/",
#         data={"name": invalid_event_name, "created_by": username_two},
#         content_type='application/json'
#     )

#     assert response.status_code == 401
#     assert not Event.objects.filter(name=invalid_event_name).exists()


#     # 5. User successfully deletes their own event
#     response = client.delete(
#        f"/v1/events/events/{event.id}/",
#         data={"name": new_event_name, "created_by": username_one},
#         content_type='application/json'
#     )

#     assert response.status_code == 200
#     assert not Event.objects.filter(name=new_event_name).exists()
