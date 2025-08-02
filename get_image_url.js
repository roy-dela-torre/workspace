// Select the <ul> element by its classes
const ul = document.querySelector('.images');

// Get all <img> elements within this <ul>
const images = ul ? ul.querySelectorAll('img') : [];

// Extract the 'src' attribute from each <img>
const imageUrls = Array.from(images).map(img => img.src);

console.log(imageUrls);