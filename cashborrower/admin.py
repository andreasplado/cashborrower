from django.contrib import admin
from .models import Lender, Borrower, Loan, LoanLike, LoanComment, LoanCommentLike, Log
# Register your models here.

admin.site.register(Lender)
admin.site.register(Borrower)
admin.site.register(Loan)
admin.site.register(LoanLike)
admin.site.register(LoanComment)
admin.site.register(LoanCommentLike)
admin.site.register(Log)



