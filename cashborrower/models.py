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
    creditcount = models.IntegerField(default=0)
    discreditcount = models.IntegerField(default=0)
    isUserVoted = models.BooleanField(default=False)
    isPrivateLoan = models.BooleanField(default=True)



class LoanVote(models.Model):
    loan = models.ForeignKey(Loan)
    lender =  models.ForeignKey(Lender)

class Log(models.Model):
    lender = models.ForeignKey(Lender)
    borrower = models.ForeignKey(Borrower)
    sum = models.FloatField(default=0.0)
    isLoanLended = models.BooleanField(default=False)
    isLoanReturned = models.BooleanField(default=False)

class Comment(models.Model):
    loan = models.ForeignKey(Loan)
    comment = models.CharField(max_length=100)
    def __str__(self):
        return self.comment

class LoanCredit(models.Model):
    loan = models.ForeignKey(Loan)
    credit = models.BooleanField(default=False)

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    like = models.BooleanField(default=False)


