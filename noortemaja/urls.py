"""noortemaja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from cashborrower.views import(
    loan_views,
    lender_views,
    lenderloan_views,
    borrower_views,
    loanlike_views,
    lenderlog_views,
    lenderloancredit_views,

)
from django.conf.urls import include, url


admin.autodiscover()
urlpatterns = [

    # ADMIN #
    url(r'^admin/', admin.site.urls),

    # LOAN #
    url(r'^loans/', loan_views.LoanListView.as_view()),
    url(r'^loan/(?P<id>[0-9]+)', loan_views.LoanDetailAPIView.as_view()),
    url(r'^loan/update/(?P<id>[0-9]+)', loan_views.LoanUpdateAPIView.as_view()),
    url(r'^loan/delete/(?P<id>[0-9]+)', loan_views.LoanDeleteAPIView.as_view()),

    # LOAN VOTE #
    url(r'^loanlikes/loan/(?P<loan_fk>[0-9]+)/likes/', loanlike_views.LoanLikeListView.as_view()),
    url(r'^loanlike/loan/(?P<loan_fk>[0-9]+)/like/(?P<id>[0-9]+)', loanlike_views.LoanLikeDetailAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan_fk>[0-9]+)/like/update/(?P<id>[0-9]+)', loanlike_views.LoanLikeUpdateAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan_fk>[0-9]+)/like/delete/(?P<id>[0-9]+)', loanlike_views.LoanLikeDeleteAPIView.as_view()),

    # LOAN VOTE(PUBLIC)#
    # url(r'^loanvotes/loan/(?P<loan_id>[0-9]+)/vote/user/(?P<lender_id>[0-9]+)', loanvote_views.LoanVoteByLenderAPIView.as_view()), # TODO : not implemented yet.

    # LENDER #
    url(r'^lenders/', lender_views.LenderListView.as_view()),
    url(r'^lender/(?P<id>[0-9]+)', lender_views.LenderDetailAPIView.as_view()),
    url(r'^lender/update/(?P<id>[0-9]+)', lender_views.LenderUpdateAPIView.as_view()),
    url(r'^lender/delete/(?P<id>[0-9]+)', lender_views.LenderDeleteAPIView.as_view()),

    # LENDER LOG #
    url(r'^lenderlogs/lender/(?P<lender_fk>[0-9]+)/logs/', lenderlog_views.LenderLogListView.as_view()),
    url(r'^lenderlog/lender/(?P<lender_fk>[0-9]+)/log/(?P<id>[0-9]+)',
        lenderlog_views.LenderLogDetailAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender_fk>[0-9]+)/log/update/(?P<id>[0-9]+)',
        lenderlog_views.LenderLogUpdateAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender_fk>[0-9]+)/log/delete/(?P<id>[0-9]+)',
        lenderlog_views.LenderLogDeleteAPIView.as_view()),

    # LENDER LOAN CREDIT #
    url(r'^lenderloancredits/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credits/',
        lenderloancredit_views.LenderLoanCreditListView.as_view()),
    url(r'^lenderloandiscredits/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/discredits/',
        lenderloancredit_views.LenderLoanDiscreditListView.as_view()),
    url(r'^lenderloancredit/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credit/(?P<id>[0-9]+)',
        lenderloancredit_views.LenderLoanCreditDetailAPIView.as_view()),
    url(r'^lenderloancredit/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credit/update/(?P<id>[0-9]+)',
        lenderloancredit_views.LenderLoanCreditUpdateAPIView.as_view()),
    url(r'^lenderloancredit/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credit/delete/(?P<id>[0-9]+)',
        lenderloancredit_views.LenderLoanCreditDeleteAPIView.as_view()),

    # LENDER LOAN #
    url(r'^lenderloans/lender/(?P<lender_fk>[0-9]+)/loans/', lenderloan_views.LenderLoansListView.as_view()),
    url(r'^lenderloan/lender/(?P<lender_fk>[0-9]+)/loan/(?P<id>[0-9]+)', lenderloan_views.LenderLoanDetailAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender_fk>[0-9]+)/loan/update/(?P<id>[0-9]+)', lenderloan_views.LenderLoanUpdateAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender_fk>[0-9]+)/loan/delete/(?P<id>[0-9]+)', lenderloan_views.LenderLoanDeleteAPIView.as_view()),
    
    # SEARCH LENDER LOAN BY EMAIL #
    url(r'^searchlenderloanbyemail/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/email/(?P<borrower_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})',
        lenderloan_views.LenderLoansListViewSearchByEmail.as_view()),



    # BORROWER #
    url(r'^borrowers/', borrower_views.BorrowerListView.as_view()),
    url(r'^borrower/(?P<id>[0-9]+)', borrower_views.BorrowerDetailAPIView.as_view()),
    url(r'^borrower/update/(?P<id>[0-9]+)', borrower_views.BorrowerUpdateAPIView.as_view()),
    url(r'^borrower/delete/(?P<id>[0-9]+)', borrower_views.BorrowerDeleteAPIView.as_view()),

    # COMMENTS # (TODO: implement)
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomments/loan/(?P<loan_fk>[0-9]+)', views.CommentListView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDetailAPIView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/update/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentUpdateAPIView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/delete/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDeleteAPIView.as_view()),
]
