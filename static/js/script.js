$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('select').formSelect();
    $('.modal').modal();
    $('.carousel').carousel();
  });


  /* The following function has been taken from 
  https://www.answertabs.com/prevent-typing-whitespace-disable-spacebar-in-input-javascript/ */
  function keyPressed(){
    var key = event.keyCode || event.charCode || event.which ;
    return key;
    }