window.onload = function(){
    var add_done_recipe = document.getElementById('add_done_recipe');
    add_done_recipe.onclick = addDoneRecipe;
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