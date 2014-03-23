// expand effect on share buttons
$(document).ready(function(){
	$('footer img').load(function() {
	    $(this).data('height', this.height);
	}).bind('mouseenter mouseleave', function(e) {
	    var enter = e.type === 'mouseenter',
	        height = $(this).data('height');
	    
	    $(this).stop().animate({
	        'margin-bottom': (enter ? 10 : 0),
	        height: height * (enter ? 1.1 : 1)
	    }, 500, "easeOutQuart");
	});
});