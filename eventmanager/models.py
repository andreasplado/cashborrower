from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class Loan(models.Model):
    lender = models.CharField(max_length=100)
    loaner = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.loaner

class Comment(models.Model):
    loan = models.ForeignKey(Loan)
    comment = models.CharField(max_length=100)
    def __str__(self):
        return self.comment

class LoanCredit(models.Model):
    loanCredit = models.ForeignKey(Loan)
    credit = models.BooleanField(default=False)

class CommentLike(models.Model):
    commentLike = models.ForeignKey(Comment)
    like = models.BooleanField(default=False)


