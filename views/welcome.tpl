% rebase('base') ### This line is important!!! ###'
% import os

<main id="welcome">
	<a href="explore">
		<section>
			<h1>The Diamond Explorer</h1>
			<h2>Click to explore <span>>></span></h2>
		</section>
	</a>
	<div id="sheffield_logo">
		<img src="static/assets/University_of_Sheffield.svg">
	</div>
	<div id="siemens_logo">
		<img src="static/assets/siemens-logo-default_0.svg"><br>
		<img src="static/assets/siemens-logo-claim.png">
	</div>
</main>
<script>

% images = os.listdir('static/photos')
var images = {{!images}};
var container = document.getElementById('container');

function switchImage(container, path, images) {
	var url = function (image) {
		return 'url("'+ path.replace(/([^\/])$/, '$1/') + image +'")'
	}
	currentImage = arguments.callee.currentImage || 0;
	nextImage = (currentImage + 1) % images.length;
	container.style.backgroundImage = url(images[currentImage]);
	arguments.callee.currentImage = nextImage;
}

setInterval(function () {switchImage(container, 'static/img', images)}, 5000);

</script>