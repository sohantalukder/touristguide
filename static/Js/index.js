const destinationBtn = document.querySelector('.destination-btn');
const placeBtn = document.querySelector('.place-btn');
const destination = document.querySelector('.all-destination');
const place = document.querySelector('.place');

const startMessage = document.querySelector('.start-message-container');
const active = document.querySelector('.active-message');
const cancel = document.querySelector('.cancel-btn');
const sendMessage = document.querySelector('.messenger-container');

destinationBtn.addEventListener('click', function () {
	place.style.display = 'none';
	destination.style.display = 'block';
	destinationBtn.style.backgroundColor = 'white';
	destinationBtn.style.color = '#5fbe00';
	placeBtn.style.backgroundColor = '#d4d4d4';
	placeBtn.style.color = 'white';
});

placeBtn.addEventListener('click', function () {
	destination.style.display = 'none';
	place.style.display = 'block';
	placeBtn.style.backgroundColor = 'white';
	placeBtn.style.color = '#5fbe00';
	destinationBtn.style.backgroundColor = '#d4d4d4';
	destinationBtn.style.color = 'white';
});

destinationBtn.addEventListener('mouseover', function () {
	destinationBtn.style.backgroundColor = 'white';
	destinationBtn.style.color = '#5fbe00';
	placeBtn.style.backgroundColor = '#d4d4d4';
	placeBtn.style.color = 'white';
});
placeBtn.addEventListener('mouseover', function () {
	placeBtn.style.backgroundColor = 'white';
	placeBtn.style.color = '#5fbe00';
	destinationBtn.style.backgroundColor = '#d4d4d4';
	destinationBtn.style.color = 'white';
});

/* Message Chat */
document
	.querySelector('.active-message')
	.addEventListener('click', function () {
		active.style.display = 'none';
		cancel.style.display = 'block';
		startMessage.style.display = 'block';
	});
document.querySelector('.cancel-btn').addEventListener('click', function () {
	active.style.display = 'block';
	cancel.style.display = 'none';
	startMessage.style.display = 'none';
	sendMessage.style.display = 'none';
});

const message = () => {
	sendMessage.style.display = 'block';
	active.style.display = 'none';
	cancel.style.display = 'block';
	startMessage.style.display = 'none';
};

// Design Event

jQuery(document).ready(function ($) {
	$('.band a').on('click', function (e) {
		e.preventDefault();
		$('.thumb-previewer img').attr('src', $(this).attr('div'));
	});
});
