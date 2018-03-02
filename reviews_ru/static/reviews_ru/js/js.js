if (screen.width > 880) {
				$(document).ready(function(){
					var options = {
						offset: 68
					}
					var header = new Headhesive('.header-top', options);
				});
			}


			if (screen.width < 768) {
				$(document).ready(function(){
					
				});
			}


			$(document).ready(function(){
				var icon_menu = $('.icon_menu_block');
				var menu = $('.nav');
				('.icon_menu_block').on('click', function(e){
					e.preventDefault();
					menu.slideToggle();
				});

				$(window).resize(function(){
					var wid = $(window).width();
					if(wid > 768 && menu.is(':hidden'){
						menu.removeAttr('style');
					}
				});

			});