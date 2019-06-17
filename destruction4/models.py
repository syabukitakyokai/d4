from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=128)
    contact = models.CharField(max_length=128)


class VenueUrl(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    url = models.CharField(max_length=256)

class Act(models.Model):
    name = models.CharField(max_length=256)
    remarks = models.CharField(max_length=256)

class ActUrl(models.Model):
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    url = models.CharField(max_length=256)

class ActDescription(models.Model):
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=128)
    postfix = models.CharField(max_length=128)
    description = models.ForeignKey(Act, on_delete=models.CASCADE)

class Event(models.Model):
    name = models.CharField(max_length=256)
    host = models.ForeignKey(Act, on_delete=models.CASCADE)

class Show(models.Model):
    open_time = models.DateTimeField()
    start_time = models.DateTimeField()
    show_time = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_prefix = models.CharField(max_length=128)
    event_postfix = models.CharField(max_length=128)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    ticket_at_door = models.IntegerField('ticket purchased at the door')
    ticket_in_advance = models.IntegerField('ticket sold in advance')
    additional_fee = models.CharField(max_length=128)


class ShowAct(models.Model):
    show = models.ForeignKey(show, on_delete=models.CASCADE)
    act = models.ForeignKey(Act, on_delete=models.CASCADE)

class ShowUrl(models.Model):
    show = models.ForeignKey(show, on_delete=models.CASCADE)
    url = models.CharField(max_length=256)



