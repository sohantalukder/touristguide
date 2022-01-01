// navigation-part-js---------------------

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

const handlePopup = () => {
	const drop = document.querySelector('.drop');
	drop.style.display = 'block';
};

const removePopup = () => {
	const drop = document.querySelector('.drop');
	drop.style.display = 'none';
};

function fullMenu() {
	location.replace('././desintaion-full.html');
}
