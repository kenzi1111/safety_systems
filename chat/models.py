from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
from functools import reduce
from django.contrib.auth import get_user_model

# Userモデルインポート
from django.conf import settings
import operator


class RoomQueryset(models.QuerySet):
    def _related_user(self, user=None):
        try:
            queryset = self.filter(
                models.Q(host=user) | models.Q(participants__in=[user.pk])
            )
        except:
            queryset = self

        return queryset

    def filtering(self, user=None, keywords="", order="-created_at"):
        words = keywords.split()
        queryset = self._related_user(user=user)

        if words:
            condition = reduce(
                operator.or_, (models.Q(name__icontains=word) for word in words)
            )
            queryset = queryset.filter(condition)

        return queryset.order_by(order).distinct()


class Room(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(gettext_lazy("Room name"), max_length=255)
    description = models.TextField(gettext_lazy("Description"))
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="rooms",
        verbose_name=gettext_lazy("Participants"),
        blank=True,
    )
    created_at = models.DateTimeField(
        gettext_lazy("Created time"), default=timezone.now
    )

    objects = RoomQueryset.as_manager()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.name

    def set_host(self, user=None):
        if user is not None:
            self.host = user

    def is_host(self, user=None):
        return user is not None and self.host.pk == user.pk

    def is_assigned(self, user=None):
        User = get_user_model()
        try:
            _ = self.participants.all().get(pk=user.pk)
            return True
        except User.DoesNotExist:
            return self.host == user
        except Exception:
            return False


class MessageManager(models.Manager):
    def ordering(self, order="created_at"):
        return self.get_queryset().order_by(order)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages"
    )
    content = models.TextField(gettext_lazy("Content"))
    created_at = models.DateTimeField(
        gettext_lazy("Created time"), default=timezone.now
    )
    objects = MessageManager()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        name = str(self.owner)
        text = self.content[:32]

        return f"{name}:{text}"


class MessageRead(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="reads")
    reader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    read_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.reader} read {self.message} at {self.read_at}"
