// GLOBAL
var currentWidth = 1100;
var timer = false;

$(function(){
	$(window).load(blocksit_set);
	//window resize

	$(window).resize(function() {
		if (timer !== false) {
			clearTimeout(timer);
		}

		timer = setTimeout(function() {
			blocksit_set();
		}, 200);
    });

	blocksit_scroll();
});

var blocksit_set = (function() {
	var winWidth = $(window).width();
	var conWidth;

	if(winWidth < 660) {
		conWidth = 440;
		col = 1;
	} else if(winWidth < 880) {
		conWidth = 660;
		col = 3;
	} else {
		conWidth = 1100;
		col = 5;
	}

	if(conWidth != currentWidth) {
		currentWidth = conWidth;
		$('#container').width(conWidth);
		$('#container').BlocksIt({
			numOfCol: col,
			offsetX: 8,
			offsetY: 8
		});
	}
});

var blocksit_scroll = (function (){
	$('#container').infinitescroll({
		navSelector  	: "#next",
		nextSelector 	: "#next",
		itemSelector 	: "#container",
		dataType	 	: 'html',
        maxPage         : 10,
		path: function(index) {
			// call setblocksit -> set_blocksit
			setTimeout(function () {
				blocksit_set();
			}, 50);

			// return filename
			return ("index" + index + ".html" + "?username=higumachan725");
		}
    });
});
