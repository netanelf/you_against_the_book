window.onload = function(){
    var add_done_recipe = document.getElementById('add_done_recipe');
    //add_done_recipe.onclick = addDoneRecipe;

    $('#add_recipe_modal').on('show.bs.modal', function (event) {
        var modal = $(this);
        var modal_inner_data = $('#add_recipe_modal_inner_data');
        $.ajax({
            url: 'add_recipe/',
            //url: "{% url 'add_recipe' %}",
            type: 'GET',
            context: document.body,
        }).done(function(response) {
            modal_inner_data.html(response);
        });
    });
    $('#add_source_modal').on('show.bs.modal', function (event) {
        var modal = $(this);
        var modal_inner_data = $('#add_source_modal_inner_data');
        $.ajax({
            url: 'add_source/',
            type: 'GET',
            context: document.body,
        }).done(function(response) {
            modal_inner_data.html(response);
        });
    });
    $('#add_making_modal').on('show.bs.modal', function (event) {
        var modal = $(this);
        var modal_inner_data = $('#add_making_modal_inner_data');
        $.ajax({
            url: 'add_making/',
            type: 'GET',
            context: document.body,
        }).done(function(response) {
            modal_inner_data.html(response);
             $('.selectpicker').selectpicker();
        });
    });
}

$(document).ready(function() {
    $("#success-alert").hide();
});

function addDoneRecipe(event, data){

    var recipe_name_e = document.getElementById('recipes_chooser');
    var recipe_making_date_e = document.getElementById('making_date');
    var recipe_rating_e = document.getElementById("rating_input")
    var recipe_effort_e = document.getElementById("effort_input")
    var recipe_comments_e = document.getElementById("making_comment")

    function onDataReceived(){
        console.log('updated site with new making');
        showAlert();
    }

    $.ajax({
        url: 'add_new_making/',
        type: 'GET',
        dataType: 'json',
        data: JSON.stringify([recipe_name_e.value,
                              recipe_making_date_e.value,
                              recipe_rating_e.value,
                              recipe_effort_e.value,
                              recipe_comments_e.value],
                              null, 2),
        success: onDataReceived
    });
}


function showAlert() {
    $("#success-alert").fadeTo(2000, 500).slideUp(500, function() {
        $("#success-alert").slideUp(500);
        });
}