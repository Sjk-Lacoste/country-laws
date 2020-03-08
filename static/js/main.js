$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    if(scroll < 350){
        $('.fixed-top').css('background', 'transparent');
    } else{
        $('.fixed-top').css('background', '#d64041');
    }
});
