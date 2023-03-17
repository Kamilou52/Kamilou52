// Func: Gn$ to CHF
// Gn$ * 0.97
function gn$ToCHF(gn$){
    return gn$ * 0.97;
}

// func: Celsius to Farenheit
// (celsius * 9/5) + 32
function celsiusToFarenheit(celsius){
    (celsius * 9/5) + 32
}

// Func: Liters to Gallons
// liters / 3.785
function litersToGallons(liters) {
    return liters / 3.785;
}


// func: Ask if the user wants to convert something
function askContinue(){
    var answer = window.prompt("Do you want to convert a value?(Yes/No)");
    if (answer.toUpperCase() == "YES") {
        return true;
    }   else {
        return false;
    }
}

// Func: Ask the type of conversion
function guessTypeconversion() {
        var answer = window.prompt("Which type of conversion?(gn$/celsius/liters)");
     
            return answer;
}
// Func: Guess user to enter a value
function askValue() {
    var answer = window.prompt("Your value Please:");
    return answer;
}
// Main:
// -continue while the user wants to convert something
// -Check which conversion
// -Get the value
// -Display the result
   
while(askContinue()) {
    var conversionType = guessTypeconversion();
    var conversionValue = askValue();
    var resultMessage = "The result is ";
    var result = 0;

    if (conversionType == "gn$") {
    resultMessage += gn$ToCHF(Number(conversionValue)).toString();
    } else if (conversionType== "celsius") {
            resultMessage += celsiusToFarenheit(Number(conversionValue)).toString();
        
    } else if (conversionType == "liters") {
            resultMessage += litersToGallons(Number(conversionValue)).toString();
        
    } else {(resultMessage == "Sorry. I can't do this coversion.");
    
    }
        console.log(resultMessage);
    }
