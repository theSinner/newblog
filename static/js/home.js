$(document).ready(imReady);

function imReady()
{
	console.log()
	console.log()
	if($(window).height()>$('#mainPlate').height())
	{
		$('#footer').addClass('abs');
	}
}
