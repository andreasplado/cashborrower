
from django.conf.urls import url
from django.contrib import admin

from cashborrower.settings import MEDIA_URL, MEDIA_ROOT
from cashborrowerAPI.views.APIviews import(

    APIviews_borrowerloan,
    APIviews_lenderloan,
    APIviews_lenderlog,
    APIviews_loancomment,
    APIviews_loanlike,
    APIviews_public_loan,
    APIviews_user,

)
from cashborrowerAPI.views.APIviews import APIviews_loandislike
from django.conf.urls import (
handler400, handler403, handler404, handler500
)
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()
urlpatterns = [

    # USERS #
    url(r'^users/', APIviews_user.UserListView.as_view()),
    url(r'^user/(?P<id>[0-9]+)', APIviews_user.UserDetailAPIView.as_view()),
    url(r'^user/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', APIviews_user.UserByEmailDetailAPIView.as_view()),
    url(r'^user/add/', APIviews_user.UserAddAPIView.as_view()),
    url(r'^username/exists/(?P<username>[^/]+)', APIviews_user.UserExistsAPIView.as_view()),
    url(r'email/exists/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', APIviews_user.EmailExistsAPIView.as_view()),
    url(r'^user/addvote/', APIviews_user.UserAddVoteAPIView.as_view()),
    url(r'^user/update/(?P<id>[0-9]+)', APIviews_user.UserUpdateAPIView.as_view()),
    url(r'^user/delete/(?P<id>[0-9]+)', APIviews_user.UserDeleteAPIView.as_view()),

    # PUBLIC LOANS #
    url(r'^publicloans/', APIviews_public_loan.PublicLoanListView.as_view()),
    url(r'^publicloan/(?P<id>[0-9]+)', APIviews_public_loan.PublicLoanDetailAPIView.as_view()),
    url(r'^publicloan/add/', APIviews_public_loan.PublicLoanAddAPIView.as_view()),
    url(r'^publicloan/update/(?P<id>[0-9]+)', APIviews_public_loan.PublicLoanUpdateAPIView.as_view()),
    #url(r'^publicloan/delete/(?P<id>[0-9]+)', public_loan_views.PublicLoanDeleteAPIView.as_view()), #DO NOT ALLOW TO DELETE PUBLIC LOANS

    # LOAN COMMENTS #
    url(r'^loancomments/loan/(?P<loan>[0-9]+)/comments/', APIviews_loancomment.LoanCommentListView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/(?P<id>[0-9]+)', APIviews_loancomment.LoanCommentDetailAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/add/', APIviews_loancomment.LoanCommentAddAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/update/(?P<id>[0-9]+)', APIviews_loancomment.LoanCommentUpdateAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/delete/(?P<id>[0-9]+)', APIviews_loancomment.LoanCommentDeleteAPIView.as_view()),


    # LOAN LIKES #
    url(r'^loanlikes/loan/(?P<loan>[0-9]+)/likes/', APIviews_loanlike.LoanLikeListView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/(?P<id>[0-9]+)', APIviews_loanlike.LoanLikeDetailAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/(?P<liker>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', APIviews_loanlike.LoanLikeByEmailDetailAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/add/', APIviews_loanlike.LoanLikeAddAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/update/(?P<id>[0-9]+)', APIviews_loanlike.LoanLikeUpdateAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/delete/(?P<id>[0-9]+)', APIviews_loanlike.LoanLikeDeleteAPIView.as_view()),

    # LOAN DISLIKES #
    url(r'^loandislikes/loan/(?P<loan>[0-9]+)/dislikes/', APIviews_loandislike.LoanDislikeListView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/(?P<id>[0-9]+)', APIviews_loandislike.LoanDislikeDetailAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/(?P<disliker>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', APIviews_loandislike.LoanDislikeByEmailAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/add/', APIviews_loandislike.LoanDislikeAddAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/update/(?P<id>[0-9]+)', APIviews_loandislike.LoanDislikeUpdateAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/delete/(?P<id>[0-9]+)', APIviews_loandislike.LoanDislikeDeleteAPIView.as_view()),

    # LOAN VOTE(PUBLIC)#
    # url(r'^loanvotes/loan/(?P<loan_id>[0-9]+)/vote/user/(?P<lender_id>[0-9]+)', loanvote_views.LoanVoteByLenderAPIView.as_view()), # TODO : not implemented yet.

    # LENDER LOG #
    url(r'^lenderlogs/lender/(?P<lender>[^/]+)/logs/', APIviews_lenderlog.LenderLogListView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/(?P<id>[0-9]+)', APIviews_lenderlog.LenderLogDetailAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/add/(?P<id>[0-9]+)', APIviews_lenderlog.LenderLogAddAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/update/(?P<id>[0-9]+)', APIviews_lenderlog.LenderLogUpdateAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/delete/(?P<id>[0-9]+)', APIviews_lenderlog.LenderLogDeleteAPIView.as_view()),



    # LENDER LOAN #

    url(r'^lenderloans/lender/(?P<lender>[^/]+)/loans/', APIviews_lenderloan.LendersLoansList.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/(?P<id>[0-9]+)', APIviews_lenderloan.LenderLoanDetailAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/add/', APIviews_lenderloan.LenderLoanAddAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/update/(?P<id>[0-9]+)', APIviews_lenderloan.LenderLoanUpdateAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/delete/(?P<id>[0-9]+)', APIviews_lenderloan.LenderLoanDeleteAPIView.as_view()),
    # SEARCH LENDER LOAN BY BORROWER EMAIL #
    url(r'^searchborrowerloanbyemail/email/(?P<borrower_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})',
        APIviews_lenderloan.LenderLoansListViewSearchByEmail.as_view()), #not working #TODO: not implemented yet


    url(r'^borrowerloans/borrower/(?P<borrower>[^/]+)/loans/', APIviews_borrowerloan.BorrowerLoansList.as_view())
]
