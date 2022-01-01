$(' .owl-one').owlCarousel({
	loop: true,
	margin: 40,
	nav: false,
	dots: true,
	autoplay: true,
	autoplayTimeout: 5000,
	slideBy: 2,
	animationIn: 'fadeIn',
	animationOut: 'fadeOut',
	responsive: {
		0: {
			items: 1,
			nav: false,
		},
		600: {
			items: 3,
		},
		1140: {
			items: 4,
		},
	},
});
$(' .owl-two').owlCarousel({
	loop: true,
	margin: 30,
	nav: false,
	dots: true,
	autoplay: true,
	autoplayTimeout: 5000,
	slideBy: 2,
	animationIn: 'fadeIn',
	animationOut: 'fadeOut',
	responsive: {
		0: {
			items: 1,
			nav: false,
		},
		600: {
			items: 3,
		},
		1140: {
			items: 3,
		},
	},
});
$(' .owl-three').owlCarousel({
	loop: true,
	margin: 30,
	nav: false,
	dots: true,
	autoplay: true,
	autoplayTimeout: 10000,
	slideBy: 2,
	animationIn: 'fadeIn',
	animationOut: 'fadeOut',
	responsive: {
		0: {
			items: 1,
			nav: false,
		},
		600: {
			items: 3,
		},
		1140: {
			items: 3,
		},
	},
});
