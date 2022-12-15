
function loadTitles(data){
	var containerList = document.getElementById("containerList");
	for (var x=0; x<data.length; x++){
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

		

		
		gradeLevelEl.innerHTML = gradeLevel;
		posterEl.src = poster;
		gameUrlEl.href =  gameurl;
		gameUrlEl.appendChild(posterEl);
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