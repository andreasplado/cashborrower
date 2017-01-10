publicLoansLenderList = [];
publicLoansBorrowerList = [];
publicLoansAmountList = [];
var cachedData;
var cachedResultsize;
var tabValue="addValue";


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
            getGivenLoans();
            break;
        case "takenLoans":
            getTakenLoans();
            break;
        case "publicLoans":
            getPublicLoans(true, false);
            break;
        case "myProfile":
            getMyProfile(true);
            break;
    }
    // this will run after every 5 seconds
}, 5000);


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

function addLoanClicks(){
    $(function () {
        $('#btn-debt-return-date').datepicker()
        .on('changeDate', function(ev){
            $('#btn-debt-return-date').empty();
            console.log(ev);
            $('#btn-debt-return-date').append(ev.date)
            $('#btn-debt-return-date').datepicker('hide');
        });
    });
    $("#btn-intrest").click(function(){
        $("#btn-intrest").hide();
        $("#intrest").show();
    });
    $("#btn-cancel-interest").click(function(){
        $("#intrest").hide();
        $("#btn-intrest").show();
    });
    $("#btn-add-loan-submit").click(function(){
        toastr["success"]("Loan added!");
    });

}

function addLoan(){
    $("#content" ).empty();
    $("#content").append('<div class="text-left" id="lender"><button type="button" class="btn btn-default" id="btn-add-loan" data-toggle="modal" data-target="#myModal">+</button></div>'
    + '<div class="modal fade" id="myModal" role="dialog">'
        + '<div class="modal-dialog">'
            + '<!-- Modal content-->'
            + '<div class="modal-content">'
                + '<div class="modal-header">'
                    + '<h4 class="modal-title">Add loan</h4>'
                + '</div>'
            + '<div class="modal-body">'
                + '<input type="text" name="username" class="form-control" id="username" placeholder="Username"></br>'
                + '<button type="button" class="btn btn-default" id="btn-debt-return-date" style="width: 100%;">DEBT RETURN DATE</button></br>'
                + '<div class="checkbox">'
                    + '<label style="float:left;"><input type="checkbox" value="">Public(seen by everybody)</label>'
                + '</div>'
                + '<button type="button" class="btn btn-default" id="btn-intrest" style="width: 100%;">INTEREST</button>'
                + '<div id="intrest" style="display:none;">'
                    + '<select class="form-control" id="intrest">'
                        + '<option>Per day</option>'
                        + '<option>Per week</option>'
                        + '<option>Per month</option>'
                        + '<option>Per year</option>'
                    + '</select>'
                    + '<input type="text" class="form-control" id="interest-interval" placeholder="%">'
                    + '<button type="button" class="btn btn-default" id="btn-cancel-interest">X</button>'
                + '</div>'
            + '</div></br>'
            + '<div class="modal-footer">'
                + '<button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>'
                + '<button type="button" class="btn btn-default" id="btn-add-loan-submit">Add</button>'
            + '</div>'
        + '</div>'
    + '</div>'
    +'</div>');
    addLoanClicks();
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

                    publicLoansLenderList.push(data.results[i].lender);
                    publicLoansBorrowerList.push(data.results[i].borrower);
                    publicLoansAmountList.push(data.results[i].amount);
                 }
             }
             if(JSON.stringify(data) != cachedData){
                 console.log(JSON.stringify(data));
                 var count = Object.keys(data).length;
                 if(isinitialized){

                    if(data.count > cachedResultsize){
                        toastr["success"]("Public loan added!");
                    }if(data.count < cachedResultsize){
                        toastr["error"]("Public loan deleted!");
                    }
                        cachedResultsize= data.count
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

function getGivenLoans (username) {
    $("#content").empty();
     $.ajax({
         type: "GET",
         url: "/cashorrower-api/borrowerloans/borrower/" + username + "/loans/",
         contentType: "application/json; charset=utf-8",
         dataType: "json",
         success: function (data, status, jqXHR) {
             // do something
             if(JSON.stringify(data) != cachedData){
                 console.log(JSON.stringify(data));
                 var count = Object.keys(data).length;
                 if(isinitialized){
                    if(data.count > cachedResultsize){
                        toastr["success"]("Public loan added!");
                    }
                    if(data.count < cachedResultsize){
                        toastr["error"]("Public loan deleted!");
                    }
                    cachedResultsize= data.count
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

function getTakenLoans (username) {
    $("#content").empty();
     $.ajax({
         type: "GET",
         url: "/cashorrower-api/borrowerloans/borrower/" + username + "/loans/",
         contentType: "application/json; charset=utf-8",
         dataType: "json",
         success: function (data, status, jqXHR) {
             // do something
             if(JSON.stringify(data) != cachedData){
                 console.log(JSON.stringify(data));
                 var count = Object.keys(data).length;
                 if(isinitialized){
                    if(data.count > cachedResultsize){
                        toastr["success"]("Public loan added!");
                    }
                    if(data.count < cachedResultsize){
                        toastr["error"]("Public loan deleted!");
                    }
                    cachedResultsize= data.count
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

function getMyProfile (username) {
    $("#content").empty();
    $("#content").append('<a href ="logout/">Logi välja</a>');
}

