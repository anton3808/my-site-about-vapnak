setTimeout(function(){
		$(".preloader").fadeOut();
}, 1000);



if (screen.width > 800) {
	$(document).ready(function(){
		var options = {
			offset: 68
		}
		var header = new Headhesive('.header-top', options);
	});
}