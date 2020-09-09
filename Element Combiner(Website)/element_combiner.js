function capitalizeFirstLetter(string) {
	return string.charAt(0).toUpperCase() + string.slice(1);
};
var NewElement = "";
var Element1 = "";
var Element2 = "";
var SuggestionNumber = 1;
var Elements = [capitalizeFirstLetter("air"), capitalizeFirstLetter("water"), capitalizeFirstLetter("earth"), capitalizeFirstLetter("fire"), capitalizeFirstLetter("energy")];
var ElementID = Elements.length + 1;
var ElementsInfo = ["Air is what we breath.", "Water is a liquid we drink.", "Earth, the very ground we stand on.", "Fire, the beggining of destruction.", "Energy, I have no idea what to say about."]

function createNewElement() {
	while(Element1 == "") {
		Element1 = capitalizeFirstLetter(prompt("What is the first element you want to combine?", "").trim());
	}
	if(Elements.includes(Element1)) {
		while(Element2 == "") {
			Element2 = capitalizeFirstLetter(prompt("What is the second element you want to combine?", "").trim().toLowerCase());
		}
		if(Elements.includes(Element2)) {
			while(NewElement == "") {
				NewElement = capitalizeFirstLetter(prompt("The name of the new element? Element " + ElementID, "").trim().toLowerCase());
			};
			if(Elements.includes(NewElement)) {
				alert("The element " + NewElement + " already exists.");
			} else {
				Elements.push(capitalizeFirstLetter(NewElement.toLowerCase()));
				alert("Element " + NewElement + " has been successfully added.");
var info = capitalizeFirstLetter(prompt("What is the info for your element?", "").toLowerCase())
ElementsInfo.push(info)
document.getElementById("elements").innerHTML = "Your Current Elements: " + Elements.join(', ');
				NewElement = "";
				ElementID = ElementID + 1
			};
			Element1 = "";
			Element2 = "";
		} else {
			alert("The element " + Element2 + " does not exist yet.");
			NewElement = "";
			Element2 = "";
			Element1 = "";
		};
	} else {
		alert("The element " + Element1 + " does not exist yet.");
		NewElement = "";
		Element1 = "";
		Element2 = "";
	};
};

function randomElement(array) {
	document.getElementById("random_element").innerHTML = "<p class='monospace'>Random element: " + array[Math.floor(Math.random() * array.length)] + "</p>"
};

function suggestionCombiner(array) {
	document.getElementById("suggestion").innerHTML = "<p class='monospace'>Suggestion #" + SuggestionNumber + ": " + array[Math.floor(Math.random() * array.length)] + " + " + array[Math.floor(Math.random() * array.length)] + "</p>"
	SuggestionNumber = SuggestionNumber + 1
};

function lastElement(array) {
	document.getElementById("last").innerHTML = "<p class='monospace'>Last Made based of last click: " + Elements[Elements.length - 1] + "</p>"
};

function search(array) {
	var number = prompt("Index of the element you are looking for? Must be a number.", "")
	try {
		if(isNaN(number)) {
			alert("Detected a non-number.")
		} else {
			number = parseInt(number)
			if(number > Elements.length) {
				alert("Number " + number + "is more than the elements available.")
			} else {
				document.getElementById("search").innerHTML = "<p class='monospace'>The element with #" + number + ": " + capitalizeFirstLetter(Elements[number - 1]) + "</p>"
			};
		}
	} catch {
		alert("Detected a non-number.");
	}
};

function removeElement(array) {
	if(array.length > 1) {
		elementToRemove = prompt("What is the index of the element you want to remove?", "")
		if(isNaN(elementToRemove)) {
			alert("Given is not an integer")
		} else if(parseInt(elementToRemove) > array.length) {
			alert("Given is too high")
		} else {
			elementToRemove = parseInt(elementToRemove) - 1
			document.getElementById("remove_element").innerHTML = "<p class='monospace'>Element removed: " + capitalizeFirstLetter(array.splice(elementToRemove, 1).join(', ')) + "</p>"
			document.getElementById("elements").innerHTML = "<p class='monospace'>Your current elements: " + capitalizeFirstLetter(array.join(', ')) + "</p>";
			ElementID = ElementID - 1
		};
	} else {
		alert("You cannot remove all elements!")
	}
};
function infoElement(array, infoarray) {
	var name = capitalizeFirstLetter(prompt("What is the name of the element?", "").toLowerCase());
document.getElementById("info").innerHTML = "<p class='monospace'>" + infoarray[array.indexOf(name)] + "</p>"
}
function popupActivate() {
	document.getElementById("popupText").classList.toggle("show")
}