tinyMCE.init({
	// General options
	mode : "textareas",
	theme : "advanced",
	extended_valid_elements: "textarea[name|class|cols|rows]", //code
	remove_linebreaks : false, //code
	plugins : "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave,codesyntax,codehighlighting",
 
	// Theme options
	theme_advanced_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect,fullscreen,code|,codeformat",
	theme_advanced_buttons2 : " codehighlighting,|,cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,|,insertdate,inserttime,preview,|,forecolor,backcolor",
	theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl",
 
	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_statusbar_location : "bottom",
	theme_advanced_resizing : true,
 
	// Example content CSS (should be your site CSS)
	//content_css : "/css/style.css",
 
	template_external_list_url : "lists/template_list.js",
	external_link_list_url : "lists/link_list.js",
	external_image_list_url : "lists/image_list.js",
	media_external_list_url : "lists/media_list.js",
 
	// Style formats
	style_formats : [
		{title : 'Bold text', inline : 'strong'},
		{title : 'Red text', inline : 'span', styles : {color : '#ff0000'}},
		{title : 'Help', inline : 'strong', classes : 'help'},
		{title : 'Table styles'},
		{title : 'Table row 1', selector : 'tr', classes : 'tablerow'}
	],
 
	width: '700',
	height: '400'
 
});



// tinyMCE.init({  
//        // General options  
//        mode: "exact",  
//        elements : "<%=txtContent.ClientID %>",  
//        theme: "advanced",  
//        plugins: "inlinepopups,fullscreen,contextmenu,emotions,table,iespell,advlink,codesyntax",  
//        convert_urls: false,  
//          
//      // Theme options  
//        theme_advanced_buttons1: "fullscreen,code,|,cut,copy,paste,|,undo,redo,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,outdent,indent,|,iespell,link,unlink,sub,sup,removeformat,cleanup,charmap,emotions,|,formatselect,fontselect,fontsizeselect,|,codeformat",  
//        theme_advanced_buttons2: "",  
//        theme_advanced_toolbar_location: "top",  
//        theme_advanced_toolbar_align: "left",  
//        theme_advanced_statusbar_location: "bottom",  
//        theme_advanced_resizing: true,  
//        extended_valid_elements: "pre[name|class]",  
//        tab_focus : ":prev,:next"  
//    });  


//codehiglithin
//tinyMCE.init({
//	mode : "textareas",
//	theme : "advanced",
//	theme_advanced_toolbar_location : "top",
//	auto_resize:false,
//	extended_valid_elements: "textarea[name|class|cols|rows]",   // Make sure you add this
//    remove_linebreaks : false,   // Make sure you add this
//	width:720,
//    plugins : 'preview,CodeHighlighting',
//    theme_advanced_toolbar_align : "right",
//    theme_advanced_buttons1_add : " fontselect,fontsizeselect,zoom",
//    theme_advanced_buttons2_add : "preview,separator,forecolor,backcolor",
//    theme_advanced_buttons3_add_before : "tablecontrols, CodeHighlighting"  // Make sure you add this
//    
//});

