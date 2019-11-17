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
			onchange="putDateTime(this.value)"
		>
		<!--p id="data">
			<div>Temperature: <span id="temperature"></span></div>
			<div>Humidity: <span id="humidity"></span></div>
			<div>CO₂: <span id="co2"></span></div>
		</p-->
		<table id="graph">
			<tr>
				<th>Temperature (°C)</th>
				<th>Humidity (%&nbsp;rel.)</th>
				<th>CO₂ (ppm)</th>
			</tr>
			<tr id="bars">
				<td><div id="temperature_bar" data-min="10" data-max="30"></div></td>
				<td><div id="humidity_bar" data-min="0" data-max="100"></div></td>
				<td><div id="co2_bar" data-min="0" data-max="1000"></div></td>
			</tr>
			<tr id="values">
				<th id="temperature"></th>
				<th id="humidity"></th>
				<th id="co2"></th>
			</tr>
		</table>
	</section>
</main>
<script>

// Date range:
// min: 1489968000000 == Mon Mar 20 2017 00:00:00 GMT+0000 (Greenwich Mean Time)
// max: 1490054395000 == Mon Mar 20 2017 23:59:55 GMT+0000 (Greenwich Mean Time)

var bars = document.querySelectorAll('#bars div');
var values = document.querySelectorAll('#values th');

var dateObject = new Date();
$.post('timestamp', function (time) {
	//var time = parseInt(response, 10);
	document.getElementById('range').value = time;
	setDateTime(time);
	fetchDateTime(time);
});

function setDateTime(time) {
	dateObject.setTime(time);
	document.getElementById('date').textContent = dateObject.toDateString();
	document.getElementById('time').textContent = dateObject.toTimeString();
}

function fetchDateTime(time) {
	$.post('fetch', {time: time}, function (response) {
		changeBar(0, response.temperature.toFixed(1));
		changeBar(1, response.humidity.toFixed(1));
		changeBar(2, response.co2.toFixed(1));
	});
}

function putDateTime(time) {
	$.post('put', {time: time}, function (response) {
		changeBar(0, response.temperature.toFixed(1));
		changeBar(1, response.humidity.toFixed(1));
		changeBar(2, response.co2.toFixed(1));
	});
}

function changeBar(index, value) {
	values[index].textContent = value;
	range = bars[index].dataset.max - bars[index].dataset.min;
	percent = 100 - (value - bars[index].dataset.min) * 100 / range;
	bars[index].style.height = percent +'%';
}

</script>