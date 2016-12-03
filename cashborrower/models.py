from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from datetime import datetime

# This code is triggered whenever a new user has been created and saved to the database
# For authentication
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.

class Loan(models.Model):
    lender = models.CharField(max_length=255)
    borrower = models.CharField(max_length=255)
    amount = models.FloatField(default=0.0)
    notes = models.CharField(max_length=255,blank=True)
    loanAdded = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    isLoanPrivate = models.BooleanField(default=False)
    interest = models.FloatField(default=0.0)
    interestInterval = models.CharField(max_length=5)

class LoanLike(models.Model):
    loan = models.ForeignKey(Loan)
    liker = models.CharField(max_length=255)

class LoanDislike(models.Model):
    loan = models.ForeignKey(Loan)
    disliker = models.CharField(max_length=255)

class LoanComment(models.Model):
    loan = models.ForeignKey(Loan)
    comment = models.CharField(max_length=100)
    commenter = models.CharField(max_length=100)

class LoanCommentLike(models.Model):
    loancomment = models.ForeignKey(LoanComment)
    liker = models.CharField(max_length=255)

class LoanCommentDislike(models.Model):
    loancomment = models.ForeignKey(LoanComment)
    disliker = models.CharField(max_length=255)

class Log(models.Model):
    lender = models.CharField(max_length=255)
    borrower = models.CharField(max_length=255)
    isLoanReturned = models.BooleanField(default=False)
    loan = models.ForeignKey(Loan)

class User(models.Model):
    gmail = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255)
    imagePath = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)


