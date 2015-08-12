//<!-- This Javascript Sheet was created by Michael Stroughair in the Summer of 2015 for the ESB Self-Healing Network model-->

var update = setInterval(function(){
	var time = document.getElementById("time").contentWindow.document.body.h1.innerHTML.match(/\d+/g);
	if (time === "9") //ie, when the fault has not been triggered
	{
		document.getElementsByClassName("chart").style.display = "none";
		document.getElementById("time").style.display = "none";
		document.getElementsByClassName("status").style.background = 'url("bar_green.png")';
		document.getElementsbyClassName("payload").style.background = 'url("fault0.png")';
	}
	else if (time === "0") //ie, just after the fault has been triggered
	{
		document.getElementsByClassName("chart").style.display = "inline";
		document.getElementById("time").style.display = "inline";
		document.getElementsByClassName("status").style.background = 'url("bar_red_h.png")';
		document.getElementsbyClassName("payload").style.background = 'url("fault1.png")';

	}
	else if (time === "1") //stages are coming back online one by one from here on out
	{
		document.getElementsByClassName("chart").style.display = "inline";
		document.getElementById("time").style.display = "inline";
		document.getElementsByClassName("status").style.background = 'url("bar_red_h.png")';
		document.getElementsbyClassName("payload").style.background = 'url("fault2.png")';

	}
	else if (time === "2")
	{
		document.getElementsByClassName("chart").style.display = "inline";
		document.getElementById("time").style.display = "inline";
		document.getElementsByClassName("status").style.background = 'url("bar_red_h.png")';
		document.getElementsbyClassName("payload").style.background = 'url("fault3.png")';
	}
	else if (time === "3")
	{
		document.getElementsByClassName("chart").style.display = "inline";
		document.getElementById("time").style.display = "inline";
		document.getElementsByClassName("status").style.background = 'url("bar_red_h.png")';
		document.getElementsbyClassName("payload").style.background = 'url("fault4.png")';
	}
}, 100)