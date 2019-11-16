% rebase('base') ### This line is important!!! ###'
% import os

<main id="welcome">
	<section>
		<h1>The Diamond Explorer</h1>
		<h2><a href="explore">Click to explore <span>>></span></a></h2>
	</section>
</main>
<script>

% images = os.listdir('static/img')
var images = {{!images}};
var background = document.body;
var foreground = document.getElementById('container');

function switchImage(background, foreground, path, images) {
	var url = function (image) {
		return 'url("'+ path.replace(/([^\/])$/, '$1/') + image +'")'
	}
	currentImage = arguments.callee.currentImage || 0;
	nextImage = (currentImage + 1) % images.length;
	background.style.backgroundImage = url(images[currentImage]);
	foreground.style.backgroundImage = url(images[nextImage]);
	arguments.callee.currentImage = nextImage;
}

switchImage(background, foreground, 'static/img', images);
setInterval(function () {switchImage(background, foreground, 'static/img', images)}, 5000);

</script>