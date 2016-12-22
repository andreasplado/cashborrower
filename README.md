# Cashborrower

### Cash borrowing system - CashBorrower.

This site is made in python for educational purpouses.
This site is offering REST application endpoints for for money lending system.
You can write whatever endpoint to this allication.
Wherever you use this site, you got domain name.
After domain name you have specified urls which are described as endpoint url in this REST implementation.
So the site that has available endpoint admin for example you have this kind of url: <b>[domainame]/admin</b>
This leads to the admin panel of that djangorestframework.

### ERD
<img src="http://phonewe.freeiz.com/cash.png" />

#### Admin panel looks like this in this current program
<img src="http://phonewe.freeiz.com/example_of_admin_panel.png">

#### Available endpoints:

* admin/
* api-token-auth/
* users/
* user/[id]
* user/[user_email]
* user/add/
* username/exists/[username]
* user/addvote/
* user/update/[id]
* user/delete/[id]
* publicloans/
* publicloan/[id]
* publicloan/add/
* publicloan/update/[id]
* loancomments/loan/[id]/comments/
* loancomment/loan/[loan_id]/comment/[id]
* loancomment/loan/[loan_id]/comment/add/
* loancomment/loan/[loan_id]/comment/update/[id]
* loancomment/loan/[loan_id]/comment/delete/[id]
* loanlikes/loan/[loan_id]/likes/
* loanlike/loan/[loan_id]/like/[id]
* loanlike/loan/[loan_id]/like/[liker_email]
* loanlike/loan/[loan_id]/like/add/
* loanlike/loan/[loan_id]/like/update/[id]
* loanlike/loan/[loan_id]/like/delete/[id]
* loandislikes/loan/[loan_id]/dislikes/
* loandislike/loan/[loan_id]/dislike/[id]
* loandislike/loan/[loan_id]/dislike/[disliker_email]
* loandislike/loan/[loan_id]/dislike/add/
* loandislike/loan/[loan_id]/dislike/update/[id]
* loandislike/loan/[loan_id]/dislike/delete/[id]
* lenderlogs/lender/[lender_email]/logs/
* lenderlog/lender/[lender_email]/log/[id]
* lenderlog/lender/[lender_email]/log/add/[id]
* lenderlog/lender/[lender_email]/log/update/[id]
* lenderlog/lender/[lender_email]/log/delete/[id]
* lenderloans/lender/[lender_email]/loans/
* lenderloan/lender/[lender_email]/loan/[id]
* lenderloan/lender/[lender_email]/loan/add/
* lenderloan/lender/[lender_email]/loan/update/[id]
* lenderloan/lender/[lender_email]/loan/delete/[id]
* searchborrowerloanbyemail/email/[borrower_email]
* borrowerloans/borrower/[borrower_email]/loans/

You can edit update and delete files.
Database is using SQLite.
You can use DBBrowser for SQLite for browsing data: http://sqlitebrowser.org/
Most of the endpoints have authorized access.
You need to recive token from the user. Every registred user have unique token inside database.
Token will  be given to the header to get authorized access for the endpoint

For unauthorized access of this kind of url [domain_name]/loanlikes/loan/18/likes/ you will not recive JSON about loan likes rather you recive message about unauthorized access and will also get HTTP 401 error - unauthorized
<img src="http://phonewe.freeiz.com/loanlikelist.png"/>

To get non-fancy palin JSON format of data from the endpoint you will add trailing slash ath the end of the url with an extra data:
 /?format=json

