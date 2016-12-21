# Cashborrower

#### Cash borrowing system - CashBorrower.

This site is made in python for educational purpouses.
This site is offering REST application endpoints for for money lending system.
You can write whatever endpoint to this allication.


### Available endpoints:
  -^admin/
  -^api-token-auth/
  -^users/
  -^user/(?P<id>[0-9]+)
  -^user/(?P<gmail>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})
  -^user/add/
  -^username/exists/(?P<username>[^/]+)
  -^user/addvote/
  -^user/update/(?P<id>[0-9]+)
  -^user/delete/(?P<id>[0-9]+)
  -^publicloans/
  -^publicloan/(?P<id>[0-9]+)
  -^publicloan/add/
  -^publicloan/update/(?P<id>[0-9]+)
  -^loancomments/loan/(?P<loan>[0-9]+)/comments/
  -^loancomment/loan/(?P<loan>[0-9]+)/comment/(?P<id>[0-9]+)
  -^loancomment/loan/(?P<loan>[0-9]+)/comment/add/
  -^loancomment/loan/(?P<loan>[0-9]+)/comment/update/(?P<id>[0-9]+)
  -^loancomment/loan/(?P<loan>[0-9]+)/comment/delete/(?P<id>[0-9]+)
  -^loanlikes/loan/(?P<loan>[0-9]+)/likes/
  -^loanlike/loan/(?P<loan>[0-9]+)/like/(?P<id>[0-9]+)
  -^loanlike/loan/(?P<loan>[0-9]+)/like/(?P<liker>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})
  -^loanlike/loan/(?P<loan>[0-9]+)/like/add/
  -^loanlike/loan/(?P<loan>[0-9]+)/like/update/(?P<id>[0-9]+)
  -^loanlike/loan/(?P<loan>[0-9]+)/like/delete/(?P<id>[0-9]+)
  -^loandislikes/loan/(?P<loan>[0-9]+)/dislikes/
  -^loandislike/loan/(?P<loan>[0-9]+)/dislike/(?P<id>[0-9]+)
  -^loandislike/loan/(?P<loan>[0-9]+)/dislike/(?P<disliker>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})
  -^loandislike/loan/(?P<loan>[0-9]+)/dislike/add/
  -^loandislike/loan/(?P<loan>[0-9]+)/dislike/update/(?P<id>[0-9]+)
  -^loandislike/loan/(?P<loan>[0-9]+)/dislike/delete/(?P<id>[0-9]+)
  -^lenderlogs/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/logs/
  -^lenderlog/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/log/(?P<id>[0-9]+)
  -^lenderlog/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/log/add/(?P<id>[0-9]+)
  -^lenderlog/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/log/update/(?P<id>[0-9]+)
  -^lenderlog/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/log/delete/(?P<id>[0-9]+)
  -^lenderloans/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loans/
  -^lenderloan/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loan/(?P<id>[0-9]+)
  -^lenderloan/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loan/add/
  -^lenderloan/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loan/update/(?P<id>[0-9]+)
  -^lenderloan/lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loan/delete/(?P<id>[0-9]+)
  -^searchborrowerloanbyemail/email/(?P<borrower_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})
  -^borrowerloans/borrower/(?P<borrower>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loans/
