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
		<div id="visualisation">
			<img src="static/img/structure.png">
			<!-- diamonds
			<img src="static/img/diamond.png" class="diamond" id="diamond0">
			<img src="static/img/diamond.png" class="diamond" id="diamond1">
			<img src="static/img/diamond.png" class="diamond" id="diamond2">
			<img src="static/img/diamond.png" class="diamond" id="diamond3">
			-->
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
				<path d="M 50 0 L 100 50 L 50 100 L 0 50 Z" fill="yellow"/>
			</svg>
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
				<path d="M 50 0 L 100 50 L 50 100 L 0 50 Z" fill="orange"/>
			</svg>
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
				<path d="M 50 0 L 100 50 L 50 100 L 0 50 Z" fill="yellow"/>
			</svg>
			<!--svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
				<path d="M 50 0 L 100 50 L 50 100 L 0 50 Z" fill="orange"/>
			</svg-->
			<img src="static/img/structure_front.png">
		</div>
		<hr>
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

// Time range:
// min: 1489968000000 == Mon Mar 20 2017 00:00:00 GMT+0000 (Greenwich Mean Time)
// max: 1490054395000 == Mon Mar 20 2017 23:59:55 GMT+0000 (Greenwich Mean Time)

var values = document.querySelectorAll('#values th');
var bars = document.querySelectorAll('#bars div');
var diamonds = document.querySelectorAll('#visualisation svg');

var diamondRanges = [
	{top: 0, bottom: 100},
	{top: 0, bottom: 100},
	{top: 0, bottom: 100},
	{top: 0, bottom: 100}
];

var timeRange = {min: 1489968000000, max: 1490054395000, range:86395000};

var dateObject = new Date();
$.post('timestamp', function (timevar) {
	//var time = parseInt(response, 10);
	document.getElementById('range').value = timevar;
	setDateTime(timevar);
	fetchDateTime(timevar);
});

function setDateTime(timevar) {
	dateObject.setTime(timevar);
	document.getElementById('date').textContent = dateObject.toDateString();
	document.getElementById('time').textContent = dateObject.toTimeString();
}

function fetchDateTime(timevar) {
	$.post('fetch', {time: timevar}, function (response) {
		var value0 = updateBar(0, response.temperature.toFixed(1));
		var value1 = updateBar(1, response.humidity.toFixed(1));
		var value2 = updateBar(2, response.co2.toFixed(1));
		//var value3 = updateBar(3, response.time.toFixed(1));
		updateDiamond(0, value0);
		updateDiamond(1, value1);
		updateDiamond(2, value2);
		//updateDiamond(3, 100 - ((timevar - timeRange.min) / timeRange));
	});
	console.log((timevar - timeRange.min) / timeRange)
}

function putDateTime(timevar) {
	$.post('put', {time: timevar}, function (response) {
		var value0 = updateBar(0, response.temperature.toFixed(1));
		var value1 = updateBar(1, response.humidity.toFixed(1));
		var value2 = updateBar(2, response.co2.toFixed(1));
		//var value3 = updateBar(3, response.time.toFixed(1));
		updateDiamond(0, value0);
		updateDiamond(1, value1);
		updateDiamond(2, value2);
		//updateDiamond(3, 100 - ((timevar - timeRange.min) / timeRange));
	});
}

function updateBar(index, value) {
	values[index].textContent = value;
	range = bars[index].dataset.max - bars[index].dataset.min;
	percent = 100 - (value - bars[index].dataset.min) * 100 / range;
	bars[index].style.height = percent +'%';
	return percent;
}

function updateDiamond(index, percent) {
	var size = diamonds[index].offsetHeight;
	var range = (diamondRanges[index].bottom - diamondRanges[index].top);
	var adjustedPercent = percent * range;
	diamonds[index].style.top = (diamondRanges[index].top + percent) +'%';
}

</script>