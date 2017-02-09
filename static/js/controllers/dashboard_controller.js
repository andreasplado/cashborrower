publicLoansLenderList = [];
publicLoansBorrowerList = [];
publicLoansAmountList = [];
var givenLoansCachedData;
var givenLoansCachedResultsize;
var takenLoansCachedData;
var takenLoansCachedResultsize;
var publicLoansCachedData;
var publicLoansCachedResultsize;
var tabValue="addValue";
var tokenObj = JSON.parse(window.localStorage.getItem('token'));
var token = "Token " + tokenObj['token'];
var username = window.localStorage.getItem('username');


$(document).ready(function(){

    tabClicks();
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "400",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
    addLoan();
setInterval(function(){

    switch(tabValue){
        case "givenLoans":
            getGivenLoans(true);
            break;
        case "takenLoans":
            getTakenLoans(true);
            break;
        case "publicLoans":
            getPublicLoans(true, false);
            break;
    }
    // this will run after every 5 seconds
}, 30000);


});

function tabClicks(){

    $('.tab').click(function () {
        $('.tabopen').removeClass('tabopen');
        $(this).addClass('tabopen');
    });
    $("#tab_add_loan").click(function(){
        addLoan();
        tabValue = "addLoan";
    });
    $("#tab_given_loans").click(function(){
        getGivenLoans();
        tabValue = "givenLoans";
    });
    $("#tab_taken_loans").click(function(){
        getTakenLoans();
        tabValue = "takenLoans";
    });
    $("#tab_public_loans").click(function(){
        getPublicLoans(true, true);
        tabValue = "publicLoans";
    });
    $("#tab_my_profile").click(function(){
        getMyProfile();
        tabValue = "myProfile";
    });

}

function getGivenLoans (isinitialized) {
    $("#content").empty();
     $.ajax({
         type: "GET",
         url: "/cashorrower-api/lenderloans/lender/" + username + "/loans/",
         headers: {"Authorization" : token},
         contentType: "application/json; charset=utf-8",
         dataType: "json",
         success: function (data, status, jqXHR) {
             // do something
             if(JSON.stringify(data) != givenLoansCachedData){
                 console.log(JSON.stringify(data));
                 var count = Object.keys(data).length;
                 if(isinitialized){
                    if(data.count > givenLoansCachedResultsize){
                        toastr["success"]("Given loan added!");
                    }
                    if(data.count < givenLoansCachedResultsize){
                        toastr["error"]("Public loan deleted!");
                    }
                    givenLoansCachedResultsize= data.count
                 }

                 $(".lender" ).remove();
                 $(".borrower").remove();

                 for(i=0; i< data.results.length; i++){
                    $("#content").append('<div class="text-left content" id="lender">'
                    + '<b class="lbl-lender">Lender:</b> ' + data.results[i].lender + '</br>'
                    + '<b class="lbl-borrower">Borrower:</b> ' + data.results[i].borrower + '</br>'
                    + '<b class="lbl-amount">Amount:</b> ' + data.results[i].amount + '</br>'
                    + '<b class="lbl-loan-reason">Loan reason:</b> ' + data.results[i].notes + '</div>'
                    );

                    //intrest
                    if(data.results[i].interest != 0){
                        $(".content").append(''
                        + '<b class="lbl-intrest">Intress:</b> ' + data.results[i].interest + ' '+ data.results[i].interestInterval +'</div>')
                    }
                    $("#content").append(''
                    + '<button type="button" class="btn btn-default" id="btn-trust">Trust</button>'
                    + '<button type="button" class="btn btn-default" id="btn-distrust">Distrust</button>');

                    publicLoansLenderList.push(data.results[i].lender);
                    publicLoansBorrowerList.push(data.results[i].borrower);
                    publicLoansAmountList.push(data.results[i].amount);
                 }
             }
             cachedData = JSON.stringify(data);
             /*$("#lender").html(
                publicLoansLenderList
             );*/


         },

         error: function (jqXHR, status) {
             // error handler
             alert("Ei päääse andmete juurde");
         }
    });
}

function getTakenLoans (isinitialized) {
    $("#content").empty();
     $.ajax({
         type: "GET",
         url: "/cashorrower-api/borrowerloans/borrower/" + username + "/loans/",
         headers: {"X-Test-Header": "test-value"},
         contentType: "application/json; charset=utf-8",
         headers: {"Authorization" : token},
         dataType: "json",
         success: function (data, status, jqXHR) {
             // do something
             if(JSON.stringify(data) != takenLoansCachedData){
                 console.log(JSON.stringify(data));
                 var count = Object.keys(data).length;
                 if(isinitialized){
                    if(data.count > takenLoansCachedResultsize){
                        toastr["success"]("Public loan added!");
                    }
                    if(data.count < takenLoansCachedResultsize){
                        toastr["error"]("Public loan deleted!");
                    }
                    takenLoansCachedResultsize= data.count
                 }

                 $(".lender" ).remove();
                 $(".borrower").remove();

                 for(i=0; i< data.results.length; i++){
                    $("#content").append('<div class="text-left content" id="lender">'
                    + '<b class="lbl-lender">Lender:</b> ' + data.results[i].lender + '</br>'
                    + '<b class="lbl-borrower">Borrower:</b> ' + data.results[i].borrower + '</br>'
                    + '<b class="lbl-amount">Amount:</b> ' + data.results[i].amount + '</br>'
                    + '<b class="lbl-loan-reason">Loan reason:</b> ' + data.results[i].notes + '</div>'
);

                    //intrest
                    if(data.results[i].interest != 0){
                        $(".content").append(''
                        + '<b class="lbl-intrest">Intress:</b> ' + data.results[i].interest + ' '+ data.results[i].interestInterval +'</div>')
                    }
                    $("#content").append(''
                    + '<button type="button" class="btn btn-default" id="btn-trust">Trust</button>'
                    + '<button type="button" class="btn btn-default" id="btn-distrust">Distrust</button>');

                    publicLoansLenderList.push(data.results[i].lender);
                    publicLoansBorrowerList.push(data.results[i].borrower);
                    publicLoansAmountList.push(data.results[i].amount);
                 }
             }
             cachedData = JSON.stringify(data);
             /*$("#lender").html(
                publicLoansLenderList
             );*/


         },

         error: function (jqXHR, status) {
             // error handler
             alert("Ei päääse andmete juurde");
         }
    });
}

function getPublicLoans (isinitialized, isClicked) {
     $.ajax({
         type: "GET",
         url: "cashorrower-api/publicloans/",
         contentType: "application/json; charset=utf-8",
         dataType: "json",
         success: function (data, status, jqXHR) {
             // do something
             if(isClicked){
                $(".content").empty();
                 for(i=0; i< data.results.length; i++){
                    $("#content").append('<div class="text-left content" id="lender">'
                    + '<b class="lbl-lender">Lender:</b> ' + data.results[i].lender + '</br>'
                    + '<b class="lbl-borrower">Borrower:</b> ' + data.results[i].borrower + '</br>'
                    + '<b class="lbl-amount">Amount:</b> ' + data.results[i].amount + '</br>'
                    + '<b class="lbl-loan-reason">Loan reason:</b> ' + data.results[i].notes + '</div>'
                    );

                    //intrest
                    if(data.results[i].interest != 0){
                        $(".content").append(''
                        + '<b class="lbl-intrest">Intress:</b> ' + data.results[i].interest + ' '+ data.results[i].interestInterval +'</div>')
                    }
                    $("#content").append(''
                    + '<button type="button" class="btn btn-default" id="btn-trust">Trust</button>'
                    + '<button type="button" class="btn btn-default" id="btn-distrust">Distrust</button>');
                 }
             }
             if(JSON.stringify(data) != publicLoansCachedData){
                 console.log(JSON.stringify(data));
                 var count = Object.keys(data).length;
                 if(isinitialized){

                    if(data.count > publicLoansCachedResultsize){
                        toastr["success"]("Public loan added!");
                    }if(data.count < publicLoansCachedResultsize){
                        toastr["error"]("Public loan deleted!");
                    }
                        publicLoansCachedResultsize= data.count
                 }
                 $(".content").empty();
                 for(i=0; i< data.results.length; i++){
                    $("#content").append('<div class="text-left content" id="lender">'
                    + '<b class="lbl-lender">Lender:</b> ' + data.results[i].lender + '</br>'
                    + '<b class="lbl-borrower">Borrower:</b> ' + data.results[i].borrower + '</br>'
                    + '<b class="lbl-amount">Amount:</b> ' + data.results[i].amount + '</br>'
                    + '<b class="lbl-loan-reason">Loan reason:</b> ' + data.results[i].notes + '</div>'
                    );

                    //intrest
                    if(data.results[i].interest != 0){
                        $(".content").append(''
                        + '<b class="lbl-intrest">Intress:</b> ' + data.results[i].interest + ' '+ data.results[i].interestInterval +'</div>')
                    }
                    $("#content").append(''
                    + '<button type="button" class="btn btn-default" id="btn-trust">Trust</button>'
                    + '<button type="button" class="btn btn-default" id="btn-distrust">Distrust</button>');

                    publicLoansLenderList.push(data.results[i].lender);
                    publicLoansBorrowerList.push(data.results[i].borrower);
                    publicLoansAmountList.push(data.results[i].amount);
                 }
             }
             cachedData = JSON.stringify(data);
             /*$("#lender").html(
                publicLoansLenderList
             );*/


         },

         error: function (jqXHR, status) {
             // error handler
             alert("Ei päääse andmete juurde");
         }
    });
}

function getMyProfile (username) {
    $("#content").empty();
    $("#content").append('<a href ="logout/" class="logout">Logi välja</a>');
    $(".logout").click(function(){
        window.localStorage.removeItem('token');
        window.localStorage.removeItem('username');
    });
}

