from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.


class Lender(models.Model):
    email = models.CharField(max_length=100)

class Borrower(models.Model):
    email = models.CharField(max_length=100)

class Loan(models.Model):
    lender = models.ForeignKey(Lender)
    borrower = models.ForeignKey(Borrower)
    amount = models.FloatField(default=0.0)
    notes = models.CharField(max_length=255,blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    isLoanReturned = models.BooleanField(default=False)

class LoanLike(models.Model):
    loan = models.ForeignKey(Loan)
    liker = models.CharField(max_length=255)
    isLiked = models.BooleanField(default=True)

class LoanComment(models.Model):
    loan = models.ForeignKey(Loan)
    comment = models.CharField(max_length=100)
    commenter = models.CharField(max_length=100)

class LoanCommentLike(models.Model):
    comment = models.ForeignKey(LoanComment)
    isLiked = models.BooleanField(default=False)

class Log(models.Model):
    lender = models.ForeignKey(Lender)
    borrower = models.ForeignKey(Borrower)
    loan = models.ForeignKey(Loan)




