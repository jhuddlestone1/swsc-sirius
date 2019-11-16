% rebase('base') ### This line is important!!! ###'

<main id="explore">
	<section>
		<h1>The Diamond Explorer</h1>
		<p>
			<span id="date"></span>
			<span id="time"></span>
		</p>
		<input
			id="range"
			type="range"
			min="1489968000000"
			max="1490054395000"
			step="5000"
			oninput="setDateTime(this.value)"
			onchange="updateDateTime(this.value)"
		>
	</section>
</main>
<script>

// Date range:
// min: 1489968000000 == Mon Mar 20 2017 00:00:00 GMT+0000 (Greenwich Mean Time)
// max: 1490054395000 == Mon Mar 20 2017 23:59:55 GMT+0000 (Greenwich Mean Time)

var dateObject = new Date();

setDateTime(document.getElementById('range').value);

function setDateTime(time) {
	dateObject.setTime(time);
	document.getElementById('date').textContent = dateObject.toDateString();
	document.getElementById('time').textContent = dateObject.toTimeString();
}

function updateDateTime(time) {
	$.post('api', {time: time});
}

</script>