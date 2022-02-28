alert("Тихонов Виктор, 4917");

function ChangeBG() {
  var body = document.getElementsByTagName('body')[0]
  var colors = [
    'cyan',
    'white',
    'yellow',
    'green',
    '#aaa',
    '#FF0066',
	  'rgb(176, 0, 0)'
  ]
  body.style.backgroundColor =
  colors[Math.floor(Math.random() * colors.length)]
}

function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =  h + ":" + m;
    setTimeout(startTime, 1000);
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}  

function alterTime() {
  clearTimeout(startTime);
  startTime = null;
  startTimeS();
}

function startTimeS() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('txt').innerHTML =  h + ":" + m + ":" + s;
  setInterval(startTimeS, 100);
}

function addRow() {
  var left = document.getElementById('c1').value;
  var right = document.getElementById('c2').value;

  var table = document.getElementById('myTable');

  var newRow = table.insertRow(1);

  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);

  cell1.innerHTML = left;
  cell2.innerHTML = right;
}

function rmRow() {
  var exterminate = document.getElementById('c3').value;

  var table = document.getElementById('myTable');

  table.deleteRow(exterminate);
}