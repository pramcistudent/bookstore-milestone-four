// Alert message timeout after 3 seconds
setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);

// base.html
// Confirm remove from cart request by user
$('.delete').click(function () {
  return confirm("Are you sure you want to remove the item from cart?");
});

// profile page & book detail page
// Multitab function for profile and review pages
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
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();