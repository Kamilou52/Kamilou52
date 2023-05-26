function onloadFun() {
    if (localStorage.length > 0) {
        const user = localStorage.getItem("username");
        if((user != undefined) && (user != null)) {
            return document.getElementById("username").innerHTML = "Welcome " + user;
        }
        else {
            return false;
        }
        return document.getElementById("username").innerHTML = "Welcome " + user;    
    }
    else {
        let userName = prompt("Please enter your name", "");
        if (userName != null) {
            document.getElementById("username").innerHTML = "Hello " + userName;
            localStorage.setItem("username", userName);
        }
        else if (userName == "") {
            document.getElementById("username").innerHTML = ""
        }
        else {
            return false;
        let user = prompt("Please enter your name", "");

        while(user == ""){
            user = prompt("Please enter your name", "");    
        }

        if(user != null){
            document.getElementById("username").innerHTML = "Hello " + user;
            localStorage.setItem("username", user);
        }       
    }
}

window.onload = onloadFun};

document.addEventListener("click", myFunction);

function myFunction() {
  document.getElementById("seenotes").innerHTML = "Hello World";
}

function storename() {
        //retrieving data
        const username = document.getElementById("username").value;
        //storing data
        
    
    }
    
    function onloadFun () {
        if ( localStorage.length > 0 ){
            const user = localStorage.getItem("username");
            return document.getElementById("username").innerHTML = user + "! Welcome back .";
    
            return document.getElementById("username").innerHTML = user + " Welcome back !";
            
        }
        else{ 
            let userName = prompt("Please enter your name","" );
            if(userName != "" ){
            //    document.getElementById("username").innerHTML = "Hello, " + userName;
            } 
            if(userName != null ){
                document.getElementById("username").innerHTML = "Hello, " + userName; 
                localStorage.setItem("username", userName);
            }
    
            else{
                return false;
            }      
        }
    
        location.href="/";    
    
        }

// const notes = ['notes:shema.sql', ];
// const para = document.querySelector('p');
// const input = document.querySelector('input');
// const bouton = document.querySelector('button');

// bouton.addEventListener('click', function() {
//   let searchnote = input.title;
//   input.value = '';
//   input.focus();
//   for (let i = 0; i < notes.length; i++) {
//     let splitnote = notes[i].split(':');
//     if (splitnote[0] === searchnote) {
//       para.textTitle = splitnote[0] + '\'s title is ' + splitnote[1] + '.';
//       break;
//     } else {
//       para.textTitle = 'Note is not found.';
//     }
//   }
// });

const output = document.querySelector('.output');
output.innerHTML = '';

let i = 4;

const para = document.createElement('p');
para.textTitle = DataTransfer ;
output.appendChild(para);
