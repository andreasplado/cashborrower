from django.contrib import admin
from .models import Loan, LoanLike, LoanComment, LoanCommentLike, LoanCommentDislike, Log, LoanDislike, User
# Register your models here.
admin.site.register(User)
admin.site.register(LoanCommentDislike)
admin.site.register(Loan)
admin.site.register(LoanLike)
admin.site.register(LoanDislike)
admin.site.register(LoanComment)
admin.site.register(LoanCommentLike)
admin.site.register(Log)



