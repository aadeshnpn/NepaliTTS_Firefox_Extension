function readoutloud_function(){
	const Cc = Components.classes;
	const Ci = Components.interfaces;
	const Cu = Components.utils;
	const Cr = Components.results;
	//var {Cc, Ci, Cu} = require("chrome");
	var {FileUtils} = Cu.import("resource://gre/modules/FileUtils.jsm");

	var file = Cc['@mozilla.org/file/local;1']
		   .createInstance(Ci.nsILocalFile);

	//file.initWithPath('C:\\temp\\temp.txt');
	//getting platform type
	getPlatform= navigator.platform.toLowerCase().split(" ");
	var platform = getPlatform[0];
	if(platform =='linux'){
		file.initWithPath("/usr/lib/cgi-bin/tts/test.txt");
		if ( file.exists() == false ) 
			file.create(Components.interfaces.nsIFile.NORMAL_FILE_TYPE, 420);
		else
			file.remove(true)
	}else if(platform =='win32' || platform == 'win16') {
		file.initWithPath("C:\\test.txt");
		if ( file.exists() == false ) 
			file.create(Components.interfaces.nsIFile.NORMAL_FILE_TYPE, 420);
	}else{
		alert("The addon is accessible only for Linux and Windows platform. Please Wait!! We are working for other");
		return;
	}

	if(!file.exists()){
	  file.create(file.NORMAL_FILE_TYPE, 0666);
	}
	
	// WRITE
	var data = content.getSelection();
	var charset = 'UTF-8';
	var fileStream = Cc['@mozilla.org/network/file-output-stream;1'].createInstance(Ci.nsIFileOutputStream);
	fileStream.init(file, FileUtils.MODE_WRONLY | FileUtils.MODE_CREATE | FileUtils.MODE_APPEND, 0x200, false);

	var converterStream = Cc['@mozilla.org/intl/converter-output-stream;1'].createInstance(Ci.nsIConverterOutputStream);

	converterStream.init(fileStream, charset, data.length,Ci.nsIConverterInputStream.DEFAULT_REPLACEMENT_CHARACTER);
	converterStream.writeString(data);
	converterStream.close();
	fileStream.close();

	//Execute CGI Script
	//document.location = "http://127.0.0.1/test/process.php?q=" + data;
	var url="http://127.0.0.1/test/process.php?q=" + data;
	var win=window.open(url,'_blank');
	win.focus();
	// READ
	var input = {};
	var inputStream = Components.classes["@mozilla.org/network/file-input-stream;1"].createInstance(Components.interfaces.nsIFileInputStream);
	var converter = Components.classes["@mozilla.org/intl/converter-input-stream;1"].createInstance(Components.interfaces.nsIConverterInputStream);
	inputStream.init(file, 0x01, 0444, null);
        converter.init(inputStream, "UTF-8", 0, 0x0000);
	converter.readString(inputStream.available(), input);
	
	alert(data + ' this is output '+input);
	
	//Delete The text file
	if(!file.exists()){
	  file.delete(file.NORMAL_FILE_TYPE);
	}
} 

