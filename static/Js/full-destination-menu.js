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

// dropdown js start--------------------

function myFunction() {
	document.getElementById('myDropdown').classList.toggle('show');
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
	if (!event.target.matches('.dropbtn')) {
		var dropdowns = document.getElementsByClassName('dropdown-content');
		var i;
		for (i = 0; i < dropdowns.length; i++) {
			var openDropdown = dropdowns[i];
			if (openDropdown.classList.contains('show')) {
				openDropdown.classList.remove('show');
			}
		}
	}
};
