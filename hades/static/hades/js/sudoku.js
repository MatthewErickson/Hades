var $table = $("#table"),
	$input = $("input"),
	$open = $(".open"),
	values = [],
	NORMAL = '#DDD',
	COMPLETE = 'green',
	ERROR = 'red';

function onChange() {
	var $ele = $(this),
		row = $ele.attr('id').charAt(0),
		col = $ele.attr('id').charAt(2);

	$ele.val($ele.val().slice(0, 1));
		
	console.log("Row: " + row + ", Col: " + col + " changed to " + $ele.val());
	values[row][col] = $ele.val();

	// check if board is solved
	var status = getBoardState();
	$open.css('background-color', status);
}

function getBoardState() {
	if (!boardIsFull()) return NORMAL;
	if (errorInRows()) return ERROR;
	if (errorInCols()) return ERROR;

	return COMPLETE;
}

function errorInRows() {
	var pos = [];
	for (var i = 0; i < 9; i++) {
		for (var j = 1; j <= 9; j++) {
			pos[j] = false;
		}
		for (var j = 0; j < 9; j++) {
			var value = values[i][j];
			if (pos[value]) {
				return true;
			}
			pos[value] = true;
		}
	}
	return false;
}

function errorInCols() {
	var pos = [];
	for (var i = 0; i < 9; i++) {
		for (var j = 1; j <= 9; j++) {
			pos[j] = false;
		}
		for (var j = 0; j < 9; j++) {
			var value = values[j][i];
			if (pos[value]) {
				return true;
			}
			pos[value] = true;
		}
	}
	return false;
}

function boardIsFull() {
	for (var i = 0; i < 9; i++) {
		for (var j = 0; j < 9; j++) {
			var $curr = $("#" + i + "-" + j);
			if (!$curr.val()) {
				return false;
			}
		}
	}
	return true;
}

$open.on('input', onChange);

// load table values into array on load
for (var i = 0; i < 9; i++) {
	values[i] = [];
	for (var j = 0; j < 9; j++) {
		var $curr = $("#" + i + "-" + j);
		values[i][j] = $curr.val();
	}
}

$(document).on('click',function(){ 
	$('.collapse').collapse('hide');
});
