const items = document.querySelectorAll(' heading ul li');
items.forEach((item) => {
	item.addEventListener('click', () => {
		document.querySelector('li.active').classList.remove('active');
		item.classList.add('active');
	});
});

// navigation.js--------------------------------------------------------

const header = document.querySelector('header');
const sectionOne = document.querySelector('.home-intro');

const sectionOneOptions = {
	rootMargin: '-200px 0px 0px 0px',
};

const sectionOneObserver = new IntersectionObserver(function (
	entries,
	sectionOneObserver
) {
	entries.forEach((entry) => {
		if (!entry.isIntersecting) {
			header.classList.add('nav-scrolled');
		} else {
			header.classList.remove('nav-scrolled');
		}
	});
},
sectionOneOptions);

sectionOneObserver.observe(sectionOne);

document.getElementById('profile-post').addEventListener('click', function () {
	document.getElementById('event-section').style.display = 'none';
	document.getElementById('profile-blog').style.display = 'block';
});
document.getElementById('event').addEventListener('click', function () {
	document.getElementById('profile-blog').style.display = 'none';
	document.getElementById('event-section').style.display = 'block';
});
