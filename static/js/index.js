$('.header').on('mouseover mouseleave', function(event){
	if (event.type === "mouseover") {
		$(this).find('ul').show();

	}else if(event.type === "mouseleave"){
		$(this).find('ul').hide();

	}
});

$('#content').ready(function(){
	for (var i = 1; i <= 15; i++) {
		if (i <= 10) {
			$('#content').append('<button class="searchbtn">' + i + '</button>');
		}else {
			$('#content').append('<button class="searchbtn">previous</button>');
			$('#content').append('<button class="searchbtn">next</button>');
			break;
		}
	}
});

$('#image').ready(function(){
var viewer = new Viewer(document.getElementById('image'));

});
