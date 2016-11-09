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

from cashborrower.views import loandislike_views
from cashborrower.views import(
    public_loan_views,
    lender_views,
    lenderloan_views,
    borrower_views,
    loanlike_views,
    lenderlog_views,
    loancomment_views,
    lendergivenloan_views,
    lendertakenloan_views

)
from django.conf.urls import include, url

admin.autodiscover()
urlpatterns = [

    # ADMIN #
    url(r'^admin/', admin.site.urls),

    # PUBLIC LOANS #
    url(r'^publicloans/', public_loan_views.PublicLoanListView.as_view()),
    url(r'^publicloan/(?P<id>[0-9]+)', public_loan_views.PublicLoanDetailAPIView.as_view()),
    url(r'^publicloan/add/', public_loan_views.PublicLoanAddAPIView.as_view()),
    url(r'^publicloan/update/(?P<id>[0-9]+)', public_loan_views.PublicLoanUpdateAPIView.as_view()),
    url(r'^publicloan/delete/(?P<id>[0-9]+)', public_loan_views.PublicLoanDeleteAPIView.as_view()),

    # LOAN COMMENTS #
    url(r'^loancomments/loan/(?P<loan>[0-9]+)/comments/', loancomment_views.LoanCommentListView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/(?P<id>[0-9]+)', loancomment_views.LoanCommentDetailAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/add/', loancomment_views.LoanCommentAddAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/update/(?P<id>[0-9]+)', loancomment_views.LoanCommentUpdateAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/delete/(?P<id>[0-9]+)', loancomment_views.LoanCommentDeleteAPIView.as_view()),


    # LOAN LIKES #
    url(r'^loanlikes/loan/(?P<loan>[0-9]+)/likes/', loanlike_views.LoanLikeListView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/(?P<id>[0-9]+)', loanlike_views.LoanLikeDetailAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/add/', loanlike_views.LoanLikeAddAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/update/(?P<id>[0-9]+)', loanlike_views.LoanLikeUpdateAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/delete/(?P<id>[0-9]+)', loanlike_views.LoanLikeDeleteAPIView.as_view()),

    # LOAN DISLIKES #
    url(r'^loandislikes/loan/(?P<loan>[0-9]+)/dislikes/', loandislike_views.LoanDislikeListView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/(?P<id>[0-9]+)',loandislike_views.LoanDislikeDetailAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/add/', loandislike_views.LoanDislikeAddAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/update/(?P<id>[0-9]+)', loandislike_views.LoanDislikeUpdateAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/delete/(?P<id>[0-9]+)', loandislike_views.LoanDislikeDeleteAPIView.as_view()),

    # LOAN VOTE(PUBLIC)#
    # url(r'^loanvotes/loan/(?P<loan_id>[0-9]+)/vote/user/(?P<lender_id>[0-9]+)', loanvote_views.LoanVoteByLenderAPIView.as_view()), # TODO : not implemented yet.

    # LENDER #
    url(r'^lenders/', lender_views.LenderListView.as_view()),
    url(r'^lender/(?P<id>[0-9]+)', lender_views.LenderDetailAPIView.as_view()),
    url(r'^lender/add/', lender_views.LenderAddAPIView.as_view()),
    url(r'^lender/update/(?P<id>[0-9]+)', lender_views.LenderUpdateAPIView.as_view()),
    url(r'^lender/delete/(?P<id>[0-9]+)', lender_views.LenderDeleteAPIView.as_view()),
    url(r'^lender/(?P<lender_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', lender_views.LenderByEmailAPIView.as_view()),

    # LENDER LOG #
    url(r'^lenderlogs/lender/(?P<lender>[0-9]+)/logs/', lenderlog_views.LenderLogListView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[0-9]+)/log/(?P<id>[0-9]+)', lenderlog_views.LenderLogDetailAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[0-9]+)/log/add/', lenderlog_views.LenderLogAddAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender_fk>[0-9]+)/log/update/(?P<id>[0-9]+)', lenderlog_views.LenderLogUpdateAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender_fk>[0-9]+)/log/delete/(?P<id>[0-9]+)', lenderlog_views.LenderLogDeleteAPIView.as_view()),


    # LENDER GIVEN LOANS #
    url(r'^lendergivenloans/lender/(?P<lender>[0-9]+)/givenloans/', lendergivenloan_views.LenderIsGivenLoanListView.as_view()),

    # LENDER TAKEN LOANS #
    url(r'^lendertakenloans/lender/(?P<lender>[0-9]+)/takenloans/', lendertakenloan_views.LenderIsTakenLoanListView.as_view()),

    # LENDER LOAN #

    # DIFFERS FOR DISPLAYING AND ADDING DATA #
    url(r'^lenderloans/lender/(?P<lender>[0-9]+)/loans/', lenderloan_views.LendersLoansList.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[0-9]+)/loan/(?P<id>[0-9]+)', lenderloan_views.LenderLoanDetailAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[0-9]+)/loan/add/', lenderloan_views.LenderLoanAddAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[0-9]+)/loan/update/(?P<id>[0-9]+)', lenderloan_views.LenderLoanUpdateAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[0-9]+)/loan/delete/(?P<id>[0-9]+)', lenderloan_views.LenderLoanDeleteAPIView.as_view()),

    # SEARCH LENDER LOAN BY EMAIL #
    url(r'^searchlenderloanbyemail/lender/(?P<lender>[0-9]+)/loan/(?P<loan>[0-9]+)/email/(?P<borrower_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})',
        lenderloan_views.LenderLoansListViewSearchByEmail.as_view()), #not working #TODO: not implemented yet.



    # BORROWER #
    url(r'^borrowers/', borrower_views.BorrowerListView.as_view()),
    url(r'^borrower/add/', borrower_views.BorrowerAddAPIView.as_view()),
    url(r'^borrower/(?P<id>[0-9]+)', borrower_views.BorrowerDetailAPIView.as_view()),
    url(r'^borrower/update/(?P<id>[0-9]+)', borrower_views.BorrowerUpdateAPIView.as_view()),
    url(r'^borrower/delete/(?P<id>[0-9]+)', borrower_views.BorrowerDeleteAPIView.as_view()),

    # COMMENTS # (TODO: implement)
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomments/loan/(?P<loan_fk>[0-9]+)', views.CommentListView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDetailAPIView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/update/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentUpdateAPIView.as_view()),
    #url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/delete/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDeleteAPIView.as_view()),
]
