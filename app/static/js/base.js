/**
* Function that tracks a click on an outbound link in Google Analytics.
* This function takes a valid URL string as an argument, and uses that URL string
* as the event label.
*/
var trackOutboundLink = function(url, new_window) {
   	ga('send', 'event', 'outbound', 'click', url, {'hitCallback':
     	function () {
     		if (!new_window) {
     			document.location = url;
     		}
     	}
   	});
	if (new_window){
		window.open(url);
	}
}

$(document).ready(function(){
	// set google analytics onclick link event on each link with class track
	$('.track').each(function(index, element){
		element = $(element);
		var link = element.attr('href');
		var new_window = element.attr('target') == '_blank' ? true : false;
		element.click(function(){
			trackOutboundLink(link, new_window);
			return false;
		})
	});
});
