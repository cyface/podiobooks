$(function(){
	
	var clearShelfCookies = function(cookie){
		$.cookie(cookie, "None", {expires: -1});
	};
		
	var gaqPush = function(shelf, titlesDeep, perSlide){
		
		var shelfPages = shelf.find(".shelf-pages");
		var threshold = parseInt(shelfPages.data("swipe-threshold"));
		
		if(!threshold){
			threshold = perSlide;
			shelfPages.data("swipe-threshold", threshold);
		}
		
		if (titlesDeep > threshold){
			threshold = titlesDeep;
			shelfPages.data("swipe-threshold", threshold);
			_gaq.push(['_trackEvent', 'Widgets', 'HomePage-ShelfTitlesDeep', shelf.find(".shelf-pages").attr("id"), (titlesDeep+1)]);
		}
	};
	
	
	// 6/8/2013 - added this to clear out old cookies
	// Can be removed later (anytime after july 2013)
	clearShelfCookies("featured_by_category");
	clearShelfCookies("top_rated_by_author");
	clearShelfCookies("recent_by_category");
	
	
	if ($("body").hasClass("home")){
		$("#featured_shelfPageContainer").pbShelf({
			//"cookie": "featured_by_category",
			"afterMoveEnd": function(titlesDeep, perSlide){
				gaqPush($("#featured_shelfPageContainer"), titlesDeep, perSlide);
			},
			"ajaxLoaderImage": siteVars("img") + "ajax-loader-bar.gif",
			"alreadyWrapped": true
		});
		
		$("#top_titles_shelfPageContainer").pbShelf({
			//"cookie": "top_rated_by_author",
			"afterMoveEnd": function(titlesDeep, perSlide){
				gaqPush($("#top_titles_shelfPageContainer"), titlesDeep, perSlide);
			},
			"ajaxLoaderImage": siteVars("img") + "ajax-loader-bar.gif",
			"alreadyWrapped": true
		});
		
		$("#recent_titles_shelfPageContainer").pbShelf({
			//"cookie": "recent_by_category",
			"afterMoveEnd": function(titlesDeep, perSlide){
				gaqPush($("#recent_titles_shelfPageContainer"), titlesDeep, perSlide);
			},
			"ajaxLoaderImage": siteVars("img") + "ajax-loader-bar.gif",
			"alreadyWrapped": true
		});
		
	}
});
