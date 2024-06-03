
function loadTitles(data){
	var containerList = document.getElementById("containerList");
	for (var x=0; x<data.length; x++){
		var channelNumber = x + 1;
		var jsonItem = data[x];
		var title =  jsonItem["title"]; 
		var gradeLevel = jsonItem["gradeLevel"];
		var poster = jsonItem["poster"]; 
		var gameurl = jsonItem["gameurl"];

		var cardContainer = document.createElement("DIV");
		cardContainer.className = "cardContainer"; 
		var gameUrlEl = document.createElement("A");
		var titleEl = document.createElement("DIV");
		var gradeLevelEl = document.createElement("DIV");
		var posterEl = document.createElement("IMG");
				posterEl.padding = "10px";

		titleEl.innerHTML = title;
		titleEl.className = "title";
		const video = document.createElement("video");

		// Set the video's attributes
		video.src = "https://rr5---sn-npoldn7e.googlevideo.com/videoplayback?expire=1717427428&ei=hIhdZqq3KJO20-kP-Yrz0QE&ip=2405%3Ada40%3A1195%3Ac000%3A9dac%3A8ee2%3A9bd1%3A2508&id=o-ABWWSAquVqF4qioKQpp9yuDEIWeZpmyq-u62BUqtbJun&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&bui=AbKP-1P2ZVp4qityzWAdpqvfBv2y7W4m_MOOIZqzfpaRxkxAP8AbP-k6ul0lB-ibVSu0pRFW4fZMuTuo&spc=UWF9f0KJx63udiT6iAYZrYG4k0spjldn93x8ltrmXLiphFZaLVMIumvnzdSQ&vprv=1&svpuc=1&xtags=heaudio%3Dtrue&mime=video%2Fmp4&ns=dJOoPIn62S4qxWj9hO5mLNkQ&rqh=1&cnr=14&ratebypass=yes&dur=2413.435&lmt=1696924459913835&c=WEB&sefc=1&txp=6218224&n=UaV2ifyd4YMOPw&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cxtags%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRAIgHCXJIYkhN9k-pxhwD_rtOhLBJqVpZK98i7tLqnjvt8ICIEhxSJgONHVJ4gtMGcatYSbLyXNpEKhI0tnwfqWGweZL&cm2rm=sn-j5aa2a0n-53ae7d,sn-ntqzl76&fexp=24350477&req_id=f097873e9bf6a3ee&redirect_counter=2&cms_redirect=yes&cmsv=e&mh=Z-&mm=34&mn=sn-npoldn7e&ms=ltu&mt=1717405463&mv=m&mvi=5&pl=41&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AHlkHjAwRAIgbGwfNnQ9EgygucfOsFdllro2MMRNay70SyemBUjuZzYCIG-C77JsernbO-xw59Uyw-Dsg_kQy0jPTAfr1Rm8t_GZ";
		video.autoplay = false;
		video.controls = true;
		video.width = 400;
		video.height = 400;
		video.padding = "10px";

		
		gradeLevelEl.innerHTML = channelNumber;
		posterEl.src = poster;
		//gameUrlEl.href =  gameurl;
		//gameUrlEl.appendChild(posterEl);
		gameUrlEl.appendChild(video);
		gameUrlEl.appendChild(titleEl);
		gameUrlEl.appendChild(gradeLevelEl);
		cardContainer.appendChild(gameUrlEl)
		containerList.appendChild(cardContainer);
		
		
		

	}
	
}

function fetchTitles(filename){
	
fetch(filename)
  .then((response) => response.json())
  .then(loadTitles);
  
}