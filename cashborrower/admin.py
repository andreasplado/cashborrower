from django.contrib import admin
from .models import Lender, Borrower, Loan, LoanLike, LoanComment, LoanCommentLike, Log, LoanDislike
# Register your models here.

admin.site.register(Lender)
admin.site.register(Borrower)
admin.site.register(Loan)
admin.site.register(LoanLike)
admin.site.register(LoanDislike)
admin.site.register(LoanComment)
admin.site.register(LoanCommentLike)
admin.site.register(Log)



