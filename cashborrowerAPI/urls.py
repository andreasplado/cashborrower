
from django.conf.urls import url
from django.contrib import admin

from cashborrower.settings import MEDIA_URL, MEDIA_ROOT
from cashborrowerAPI.views.APIviews import(

    borrowerloan,
    lenderloan,
    lenderlog,
    loancomment,
    loanlike,
    public_loan,
    user,

)
from cashborrowerAPI.views.APIviews import loandislike
from cashborrowerAPI.views.siteViews.register import account_activation_sent, activate

admin.autodiscover()
urlpatterns = [

    # USERS #
    url(r'^users/', user.UserListView.as_view()),
    url(r'^user/(?P<id>[0-9]+)', user.UserDetailAPIView.as_view()),
    url(r'^user/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', user.UserByEmailDetailAPIView.as_view()),
    url(r'^user/add/', user.UserAddAPIView.as_view()),
    url(r'^username/exists/(?P<username>[^/]+)', user.UserExistsAPIView.as_view()),
    url(r'email/exists/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', user.EmailExistsAPIView.as_view()),
    url(r'^user/addvote/', user.UserAddVoteAPIView.as_view()),
    url(r'^user/update/(?P<id>[0-9]+)', user.UserUpdateAPIView.as_view()),
    url(r'^user/delete/(?P<id>[0-9]+)', user.UserDeleteAPIView.as_view()),
    # ACTIVATE USER#
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

    # PUBLIC LOANS #
    url(r'^publicloans/', public_loan.PublicLoanListView.as_view()),
    url(r'^publicloan/(?P<id>[0-9]+)', public_loan.PublicLoanDetailAPIView.as_view()),
    url(r'^publicloan/add/', public_loan.PublicLoanAddAPIView.as_view()),
    url(r'^publicloan/update/(?P<id>[0-9]+)', public_loan.PublicLoanUpdateAPIView.as_view()),
    #url(r'^publicloan/delete/(?P<id>[0-9]+)', public_loan_views.PublicLoanDeleteAPIView.as_view()), #DO NOT ALLOW TO DELETE PUBLIC LOANS

    # LOAN COMMENTS #
    url(r'^loancomments/loan/(?P<loan>[0-9]+)/comments/', loancomment.LoanCommentListView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/(?P<id>[0-9]+)', loancomment.LoanCommentDetailAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/add/', loancomment.LoanCommentAddAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/update/(?P<id>[0-9]+)', loancomment.LoanCommentUpdateAPIView.as_view()),
    url(r'^loancomment/loan/(?P<loan>[0-9]+)/comment/delete/(?P<id>[0-9]+)', loancomment.LoanCommentDeleteAPIView.as_view()),


    # LOAN LIKES #
    url(r'^loanlikes/loan/(?P<loan>[0-9]+)/likes/', loanlike.LoanLikeListView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/(?P<id>[0-9]+)', loanlike.LoanLikeDetailAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/(?P<liker>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', loanlike.LoanLikeByEmailDetailAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/add/', loanlike.LoanLikeAddAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/update/(?P<id>[0-9]+)', loanlike.LoanLikeUpdateAPIView.as_view()),
    url(r'^loanlike/loan/(?P<loan>[0-9]+)/like/delete/(?P<id>[0-9]+)', loanlike.LoanLikeDeleteAPIView.as_view()),

    # LOAN DISLIKES #
    url(r'^loandislikes/loan/(?P<loan>[0-9]+)/dislikes/', loandislike.LoanDislikeListView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/(?P<id>[0-9]+)', loandislike.LoanDislikeDetailAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/(?P<disliker>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', loandislike.LoanDislikeByEmailAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/add/', loandislike.LoanDislikeAddAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/update/(?P<id>[0-9]+)', loandislike.LoanDislikeUpdateAPIView.as_view()),
    url(r'^loandislike/loan/(?P<loan>[0-9]+)/dislike/delete/(?P<id>[0-9]+)', loandislike.LoanDislikeDeleteAPIView.as_view()),

    # LOAN VOTE(PUBLIC)#
    # url(r'^loanvotes/loan/(?P<loan_id>[0-9]+)/vote/user/(?P<lender_id>[0-9]+)', loanvote_views.LoanVoteByLenderAPIView.as_view()), # TODO : not implemented yet.

    # LENDER LOG #
    url(r'^lenderlogs/lender/(?P<lender>[^/]+)/logs/', lenderlog.LenderLogListView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/(?P<id>[0-9]+)', lenderlog.LenderLogDetailAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/add/(?P<id>[0-9]+)', lenderlog.LenderLogAddAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/update/(?P<id>[0-9]+)', lenderlog.LenderLogUpdateAPIView.as_view()),
    url(r'^lenderlog/lender/(?P<lender>[^/]+)/log/delete/(?P<id>[0-9]+)', lenderlog.LenderLogDeleteAPIView.as_view()),



    # LENDER LOAN #

    url(r'^lenderloans/lender/(?P<lender>[^/]+)/loans/', lenderloan.LendersLoansList.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/(?P<id>[0-9]+)', lenderloan.LenderLoanDetailAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/add/', lenderloan.LenderLoanAddAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/update/(?P<id>[0-9]+)', lenderloan.LenderLoanUpdateAPIView.as_view()),
    url(r'^lenderloan/lender/(?P<lender>[^/]+)/loan/delete/(?P<id>[0-9]+)', lenderloan.LenderLoanDeleteAPIView.as_view()),
    # SEARCH LENDER LOAN BY BORROWER EMAIL #
    url(r'^searchborrowerloanbyemail/email/(?P<borrower_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})',
        lenderloan.LenderLoansListViewSearchByEmail.as_view()), #not working #TODO: not implemented yet


    url(r'^borrowerloans/borrower/(?P<borrower>[^/]+)/loans/', borrowerloan.BorrowerLoansList.as_view())
]
