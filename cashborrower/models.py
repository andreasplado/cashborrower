from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class Loan(models.Model):
    lender = models.CharField(max_length=255)
    borrower = models.CharField(max_length=255)
    amount = models.FloatField(default=0.0)
    notes = models.CharField(max_length=255,blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    isLoanPrivate = models.BooleanField(default=False)

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
    loan = models.ForeignKey(Loan)




