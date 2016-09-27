var showName = '{{ show.name }}',
	video = $("#video"),
	sourceMp4 = $("#source-mp4"),
	sourceMkv = $("#source-mkv"),
	anchor = $("#videoAnchor");

video.addClass('gone');

function loadEpisode(url) {
	video.removeClass('gone');

	sourceMp4.attr("src", url);
	sourceMkv.attr("src", url);
	
	video[0].load();
	$('html, body').animate({
		scrollTop: anchor.offset().top
	}, 1000);
	video[0].play();
}