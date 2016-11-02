from django.contrib import admin
from .models import Loan, LoanVote, LoanCredit, Comment, CommentLike, Log, Lender, Borrower
# Register your models here.

admin.site.register(Log)
admin.site.register(CommentLike)
admin.site.register(Comment)
admin.site.register(LoanCredit)
admin.site.register(Loan)
admin.site.register(LoanVote)
admin.site.register(Lender)
admin.site.register(Borrower)



