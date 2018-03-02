//...........................................................................
// ..............код для мобильного меню нашей страницы......................
//...........................................................................
jQuery(document).ready(function($){
	//move nav element position according to window width
	moveNavigation();
	$(window).on('resize', function(){
		(!window.requestAnimationFrame) ? setTimeout(moveNavigation, 300) : window.requestAnimationFrame(moveNavigation);
	});

	//mobile version - open/close navigation
	$('.cd-nav-trigger').on('click', function(event){
		event.preventDefault();
		if($('header').hasClass('nav-is-visible')) $('.moves-out').removeClass('moves-out');
		
		$('header').toggleClass('nav-is-visible');
		$('.cd-main-nav').toggleClass('nav-is-visible');
		$('.cd-main-content').toggleClass('nav-is-visible');
	});

	//mobile version - go back to main navigation
	$('.go-back').on('click', function(event){
		event.preventDefault();
		$('.cd-main-nav').removeClass('moves-out');
	});

	//open sub-navigation
	$('.cd-subnav-trigger').on('click', function(event){
		event.preventDefault();
		$('.cd-main-nav').toggleClass('moves-out');
	});

	function moveNavigation(){
		var navigation = $('.cd-main-nav-wrapper');
  		var screenSize = checkWindowWidth();
        if ( screenSize ) {
        	//desktop screen - insert navigation inside header element
			navigation.detach();
			navigation.insertBefore('.cd-nav-trigger');
		} else {
			//mobile screen - insert navigation after .cd-main-content element
			navigation.detach();
			navigation.insertAfter('.cd-main-content');
		}
	}

	function checkWindowWidth() {
		var mq = window.getComputedStyle(document.querySelector('header'), '::before').getPropertyValue('content').replace(/"/g, '');
		return ( mq == 'mobile' ) ? false : true;
	}
});













// код для выбора языка нашей страницы
$(document).ready(function(){
	$(".language_country_header").bind("click", function(){
		$('.languages_ul').show();
		$('#language_country_header').addClass('language_country_header_active');
		$('#language_country_header').removeClass('language_country_header');
	});


	$(".languages_ul").on('mouseleave',function(){
		$('.languages_ul').hide();
		$('#language_country_header').addClass('language_country_header');
		$('#language_country_header').removeClass('language_country_header_active');
	});


	$('#russia_langua').on('mouseover',function(){
		$(this).addClass('russia_langua_active');
		$('#russia_langua a').addClass('russia_langua_a_hover');
	});
	$('#ukrainian_langua').on('mouseover',function(){
		$(this).addClass('ukrainian_langua_active');
		$('#ukrainian_langua a').addClass('ukrainian_langua_a_hover');
	});




	$('#russia_langua').on('mouseout',function(){
		$(this).removeClass('russia_langua_active');
		$('#russia_langua a').removeClass('russia_langua_a_hover');
	});
	$('#ukrainian_langua').on('mouseout',function(){
		$(this).removeClass('ukrainian_langua_active');
		$('#ukrainian_langua a').removeClass('ukrainian_langua_a_hover');
	});
});