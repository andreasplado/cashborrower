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
from cashborrower import views
from cashborrower.allviews import(
    loanviews,
    lenderviews,
    lenderloanviews,
    borrowerviews,
    loanvotesview,
    lenderlogviews,
    lendercreditviews,

)
from django.conf.urls import include, url


admin.autodiscover()
urlpatterns = [

    # ADMIN #
    url(r'^admin/', admin.site.urls),

    # LOAN #
    url(r'^loans/', loanviews.LoanListView.as_view()),
    url(r'^loan/(?P<id>[0-9]+)', loanviews.LoanDetailAPIView.as_view()),
    url(r'^loan/update/(?P<id>[0-9]+)', loanviews.LoanUpdateAPIView.as_view()),
    url(r'^loan/delete/(?P<id>[0-9]+)', loanviews.LoanDeleteAPIView.as_view()),
    
    # LOAN VOTE #
    url(r'^loanvotes/loan/(?P<loan_fk>[0-9]+)/votes/', loanvotesview.LoanVotesListView.as_view()),
    url(r'^loanvotes/loan/(?P<loan_fk>[0-9]+)/vote/(?P<id>[0-9]+)', loanvotesview.LoanVoteDetailAPIView.as_view()),
    url(r'^loanvotes/loan/(?P<loan_fk>[0-9]+)/vote/update/(?P<id>[0-9]+)', loanvotesview.LoanVoteUpdateAPIView.as_view()),
    url(r'^loanvotes/loan/(?P<loan_fk>[0-9]+)/vote/delete/(?P<id>[0-9]+)', loanvotesview.LoanVoteDeleteAPIView.as_view()),

    # LOAN VOTES(PUBLIC)#
    url(r'^loanvotes/loan/(?P<loan_id>[0-9]+)/vote/user/(?P<lender_id>[0-9]+)', loanvotesview.LoanVoteByLenderAPIView.as_view()), # TODO : not implemented yet.

    # LENDER LOANS #
    url(r'^lenderloans/lender/(?P<lender_fk>[0-9]+)/loans/', lenderloanviews.LenderLoansListView.as_view()),
    url(r'^lenderloans/lender/(?P<lender_fk>[0-9]+)/loan/(?P<id>[0-9]+)', lenderloanviews.LenderLoanDetailAPIView.as_view()),
    url(r'^lenderloans/lender/(?P<lender_fk>[0-9]+)/loan/update/(?P<id>[0-9]+)', lenderloanviews.LenderLoanUpdateAPIView.as_view()),
    url(r'^lenderloans/lender/(?P<lender_fk>[0-9]+)/loan/delete/(?P<id>[0-9]+)', lenderloanviews.LenderLoanDeleteAPIView.as_view()),
    url(r'^lenderloans/lender/(?P<lender_fk>[0-9]+)/email/(?P<borrower_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', lenderloanviews.LenderLoansListViewSearchByEmail.as_view()),

    # LENDER #
    url(r'^lenders/', lenderviews.LenderListView.as_view()),
    url(r'^lender/(?P<id>[0-9]+)', lenderviews.LenderDetailAPIView.as_view()),
    url(r'^lender/update/(?P<id>[0-9]+)', lenderviews.LenderUpdateAPIView.as_view()),
    url(r'^lender/delete/(?P<id>[0-9]+)', lenderviews.LenderDeleteAPIView.as_view()),

    # LENDER LOG #
    url(r'^lenderlogs/lender/(?P<lender_fk>[0-9]+)/logs/', lenderlogviews.LenderLogListView.as_view()),
    url(r'^lenderlogs/lender/(?P<lender_fk>[0-9]+)/log/(?P<id>[0-9]+)', lenderlogviews.LenderLogDetailAPIView.as_view()),
    url(r'^lenderlogs/lender/(?P<lender_fk>[0-9]+)/log/update/(?P<id>[0-9]+)', lenderlogviews.LenderLogUpdateAPIView.as_view()),
    url(r'^lenderlogs/lender/(?P<lender_fk>[0-9]+)/log/delete/(?P<id>[0-9]+)', lenderlogviews.LenderLogDeleteAPIView.as_view()),
    
    # LENDER LOAN CREDIT #
    url(r'^lenderloancredits/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credits/', lendercreditviews.LenderCreditListView.as_view()),
    url(r'^lenderloancredits/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/discredits/', lendercreditviews.LenderDiscreditListView.as_view()),
    url(r'^lenderloancredits/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credit/(?P<id>[0-9]+)', lendercreditviews.LenderCreditDetailAPIView.as_view()),
    url(r'^lenderloancredits/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credit/update/(?P<id>[0-9]+)', lendercreditviews.LenderCreditUpdateAPIView.as_view()),
    url(r'^lenderloancredits/lender/(?P<lender_fk>[0-9]+)/loan/(?P<loan_fk>[0-9]+)/credit/delete/(?P<id>[0-9]+)', lendercreditviews.LenderCreditDeleteAPIView.as_view()),

    # BORROWER #
    url(r'^borrowers/', borrowerviews.BorrowerListView.as_view()),
    url(r'^borrower/(?P<id>[0-9]+)', borrowerviews.BorrowerDetailAPIView.as_view()),
    url(r'^borrower/update/(?P<id>[0-9]+)', borrowerviews.BorrowerUpdateAPIView.as_view()),
    url(r'^borrower/delete/(?P<id>[0-9]+)', borrowerviews.BorrowerDeleteAPIView.as_view()),

    # COMMENTS # (TODO: implement)
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomments/loan/(?P<loan_fk>[0-9]+)', views.CommentListView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDetailAPIView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/update/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentUpdateAPIView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/delete/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDeleteAPIView.as_view()),
]
