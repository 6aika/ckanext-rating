$('.rating-star').hover(
  function(){ 
    $(this).addClass('rating-star-hover');
    $(this).prevAll().addClass('rating-star-hover') ;
  },
  function(){ 
    $(this).removeClass('rating-star-hover');
    $(this).prevAll().removeClass('rating-star-hover');
  }
)
