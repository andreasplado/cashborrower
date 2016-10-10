from django.contrib import admin
from .models import Loan, LoanCredit, Comment, CommentLike, Log
# Register your models here.

admin.site.register(Log)
admin.site.register(CommentLike)
admin.site.register(Comment)
admin.site.register(LoanCredit)
admin.site.register(Loan)



