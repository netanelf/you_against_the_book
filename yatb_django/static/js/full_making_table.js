
$(document).ready(function () {
    $('#full_making_table').DataTable(
        {paging: false,
        }
    );
    $('.dataTables_length').addClass('bs-select');


    $("#create-book").modalForm({
        formURL: "edit_making/"
    });

});


function editMaking(event, data){
    console.log('editMaking');
    $(this).modalForm({
        formURL: "edit_making/"
    });
}

/*
$(function(){
    $('#login').popover({
        placement: 'bottom',
        title: 'Edit making',
        html:true,
        content:  $('#myForm').html()
    }).on('click', function(){
        // had to put it within the on click action so it grabs the correct info on submit
        $('.btn-primary').click(function(){
            $('#result').after("form submitted by " + $('#email').val())
            $.post('/echo/html/',  {
                email: $('#email').val(),
                name: $('#name').val(),
                gender: $('#gender').val()
            }, function(r){
                $('#pops').popover('hide')
                $('#result').html('resonse from server could be here' )
            })
        })
    })
})
*/

