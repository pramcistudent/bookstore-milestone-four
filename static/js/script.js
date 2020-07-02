/* 
* Multitab function for profile and review page
*/
function multiTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

$(document).ready(function () {
    /*
    * Confirmation pop up to remove item from cart
    */
    $('.delete').click(function () {
        return confirm("Are you sure you want to remove the item from cart?");
    });

    if ($('#message').length > 0) {
        setTimeout(function () {
            $('#message').remove();
        }, 3000);
    }

    // Get the element with id="defaultOpen" and click on it
    document.getElementById("defaultOpen").click();
});
