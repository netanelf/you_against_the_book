
window.onload = function(){
    var get_random_recipe = document.getElementById('get_rand_recipe');
    get_random_recipe.onclick = updateRandomRecipe;

    $('#modal').on('show.bs.modal', function (event) {
        var modal = $(this)
        $.ajax({
            //url: 'get_comments/3',
            url: generete_comment_url(3),
            context: document.body,
            //data: JSON.stringify(['only_unmade', only_unmade], null, 2),
        }).done(function(response) {
            modal.html(response);
        });
    })

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





