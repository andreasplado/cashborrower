from django.contrib import admin
from .models import Loan, LoanCredit, Comment, CommentLike
# Register your models here.

admin.site.register(Loan)
admin.site.register(LoanCredit)
admin.site.register(Comment)
admin.site.register(CommentLike)