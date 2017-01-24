var tokenObj = JSON.parse(window.localStorage.getItem('token'));
var token = "Token " + tokenObj['token']
var loanCounter = 0;


function addLoanClicks(){
    $(function () {
        $('#btn-debt-return-date').datepicker()
        .on('changeDate', function(ev){
            $('#btn-debt-return-date').empty();
            console.log(ev);
            var date = ev.date;
            var formattedDate = moment(date).format('YYYY-MM-DD');
            $('#btn-debt-return-date').append(formattedDate)
            $('#btn-debt-return-date').datepicker('hide');
        });
    });
    $("#btn-intrest").click(function(){
        $("#btn-intrest").hide();
        $("#intrest-layout").show();
    });
    $("#btn-add-loan-cancel").click(function(){
        $("#username").val("");
        $("#btn-debt-return-date").text("DEBT RETURN DATE");
        $('#cb-is-public').prop('checked', false);
        $('#interest').val("");
        $('#interest-interval').val($("#target option:first").val());
        $("#intrest-interval").val($("#intrest-interval option:first").val());
        $("#btn-intrest").show();
        $("#intrest-layout").hide();
    });
    $("#btn-cancel-interest").click(function(){
        $("#intrest-layout").hide();
        $("#btn-intrest").show();


    });
    $("#btn-add-loan-submit").click(function(){
        var username = $("#username").val();
        var debtReturnDate = $("#btn-debt-return-date").text();
        var isPublic = $('#cb-is-public').is(':checked');
        var interest = $('#interest').val();
        if(username == ""){
            toastr["error"]("Please enter the username!");
        }
        if(username != ""){
            validateData(username);
        }

    });

    $("#btn-add-loan-item").click(function(){
        // if there are more loans than 0
        if(loanCounter > 0){
            //Dont show alertbox
            $("#btn-add-loan-item").removeAttr( "data-target" );
            loanCounter++;
            addLoanItem(false);

        }else{
            //Show alert box
            $("#btn-add-loan-item").attr( "data-target", "#myModal" );
            loanCounter++;
        }
    });

}

function addLoan(){
    $("#content").empty();
    $("#content").append('<div class="text-left" id="lender">'
    + '<div class="row">'
        +'<div class="col-xs-7">'
            + '<button type="button" class="btn btn-default" id="btn-add-loan-item" data-toggle="modal" data-target="#myModal">+</button>'
        + '</div>'
        + '<div class="col-xs-2" id="remove-loan-btn-layout">'
        + '</div>'
    + '</div>'
    + ''
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
                    + '<label style="float:left;"><input type="checkbox" value="" id="cb-is-public">Public(seen by everybody)</label>'
                + '</div>'
                + '<button type="button" class="btn btn-default" id="btn-intrest" style="width: 100%;">INTEREST</button>'
                + '<div id="intrest-layout" style="display:none;">'
                    + '<select class="form-control" id="intrest-interval">'
                        + '<option>Per day</option>'
                        + '<option>Per week</option>'
                        + '<option>Per month</option>'
                        + '<option>Per year</option>'
                    + '</select>'
                    + '<input type="text" class="form-control" id="interest" placeholder="%">'
                    + '<button type="button" class="btn btn-default" id="btn-cancel-interest">X</button>'
                + '</div>'
            + '</div></br>'
            + '<div class="modal-footer">'
                + '<button type="button" class="btn btn-default" id="btn-add-loan-cancel" data-dismiss="modal">Cancel</button>'
                + '<button type="button" class="btn btn-default" id="btn-add-loan-submit">Add</button>'
            + '</div>'
        + '</div>'
    + '</div>'
    +'</div>');
    addLoanClicks();
}

function validateData(username){
     $.ajax({
         type: "GET",
         url: "cashorrower-api/username/exists/" + username + "/?format=json",
         contentType: "application/json; charset=utf-8",
         dataType: "json",
         success: function (data, status, jqXHR) {
            console.log(data);
            if(data.count== 0){
                toastr["error"]("Username does not exist!");
            }else{
                var lendername = $("#username").val();
                var debtReturnDate = $("#btn-debt-return-date").text();
                var isPublic = $('#cb-is-public').is(':checked');
                var interest = $('#interest').val();
                var interestInterval = $('#interest-interval option:selected').text();

                if(debtReturnDate == 'DEBT RETURN DATE'){
                    toastr["error"]("Please select debt return date!");
                }
                if($("#intrest-interval").is(":visible")){
                    if(interest==""){
                        toastr["error"]("Please enter the intrest!");
                    }
                }
                if(username != "" && debtReturnDate != 'DEBT RETURN DATE' ){
                    //IF ALL GOES WELL ADD ITEM
                    addLoanItem(true);

                }
            }
         },

         error: function (jqXHR, status) {
             // error handler
             alert("Ei päääse andmete juurde");
             return false;
         }
    });
}


function addLoanItem(isFirstItem){

    if(isFirstItem){
        $("#content").append(''
            + '<div class="row loan-row-'+ loanCounter +'">'
                +'<div class="col-xs-7">'
                    + '<input type="text" class="form-control" id="loan-reason-'+ loanCounter +'" placeholder="Loan reason">'
                + '</div>'
                + '<div class="col-xs-2">'
                    + '<input type="text" class="form-control" id="sum" placeholder="Sum">'
                + '</div>'
                + '</div>');
            $("#remove-loan-btn-layout").append('<button type="button" class="btn btn-default" id="btn-remove-loan-item" data-toggle="modal">-</button>');
        $('#myModal').modal('hide');
    }else{
        $("#content").append(''
            + '<div class="row loan-row-'+ loanCounter +'">'
                +'<div class="col-xs-7">'
                    + '<input type="text" class="form-control" id="loan-reason-'+ loanCounter +'" placeholder="Loan reason">'
                + '</div>'
                + '<div class="col-xs-2">'
                    + '<input type="text" class="form-control" id="sum" placeholder="Sum">'
                + '</div>'
                + '</div>');
    }
    $("#btn-remove-loan-item").click(function(){
        if(loanCounter > 0){
            loanCounter--;
            console.log("Removing");

            $(".row loan-row-"+ loanCounter).remove();

        }
        if(loanCounter == 0){
            $("#btn-remove-loan-item").remove();
        }
    });
}

function removeLoanItem(){
}




function postDataToPythonServer(){
    $.ajax({
         type: "POST",
         url: "lenderloan/lender/" + username + "/loan/add/?format=json",
         contentType: "application/json; charset=utf-8",
         headers: {"Authorization" : token},
         dataType: "json",

         success: function (data, status, jqXHR) {

         },

         error: function (jqXHR, status) {
             // error handler
             alert("Ei päääse andmete juurde");
             return false;
         }
    });
}

