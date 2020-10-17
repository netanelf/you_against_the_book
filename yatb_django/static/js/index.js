
window.onload = function(){
    var get_random_recipe = document.getElementById('get_rand_recipe');
    get_random_recipe.onclick = updateRandomRecipe;

    var add_done_recipe = document.getElementById('add_done_recipe');
    add_done_recipe.onclick = addDoneRecipe;

}


$(document).ready(function() {
    $("#success-alert").hide();
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


function updateRandomRecipe(event, data){
    function onDataReceived(recipe){
        console.log('retrieving recipe: ' + recipe.name + recipe.page);
        var c = document.getElementById("random_recipe_name");
        c.innerHTML = recipe.name;
        var c = document.getElementById("random_recipe_page_num");
        c.innerHTML = recipe.page;
        var c = document.getElementById("random_recipe_rank");
        c.innerHTML = recipe.rank;
        var c = document.getElementById("random_recipe_effort");
        c.innerHTML = recipe.effort;
    }

    var only_unmade = document.getElementById("random_only_unmade").checked;

    $.ajax({
        url: 'getRandomRecipe/',
        type: 'GET',
        dataType: 'json',
        data: JSON.stringify(['only_unmade', only_unmade], null, 2),
        success: onDataReceived
    });
}


function addDoneRecipe(event, data){

    var recipe_name_e = document.getElementById('recipes_chooser');
    var recipe_making_date_e = document.getElementById('making_date');
    var recipe_rating_e = document.getElementById("rating_input")
    var recipe_effort_e = document.getElementById("effort_input")

    function onDataReceived(){
        console.log('updated site with new making');
        showAlert();
    }

    $.ajax({
        url: 'add_new_making/',
        type: 'GET',
        dataType: 'json',
        data: JSON.stringify([recipe_name_e.value, recipe_making_date_e.value, recipe_rating_e.value, recipe_effort_e.value], null, 2),
        success: onDataReceived
    });
}


function showAlert() {
    $("#success-alert").fadeTo(2000, 500).slideUp(500, function() {
        $("#success-alert").slideUp(500);
        });
}


