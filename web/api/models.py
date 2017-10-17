# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from . import managers

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = managers.MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

# Profile
# settings.AUTH_USER_MODEL


# Organization
class Organization(models.Model):
    active = models.BooleanField(default=True)

    name = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.name

class Tag(models.Model):
    title = models.CharField(max_length=50, blank=True, default="")

    def __str__(self):
        return self.title

# Task / job / role
class Task(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100, blank=True, default="")
    tags = models.ManyToManyField(Tag)
    description = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.organization.name, self.title)
