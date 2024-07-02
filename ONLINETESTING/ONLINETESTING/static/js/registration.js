 
function validation()
{
 formm =document.getElementById("form");
 usernamee =document.getElementById("username");
 emaill =document.getElementById("email");
 phonee =document.getElementById("phone");
 passwordd =document.getElementById("password");
 cpasswordd =document.getElementById("cpassword");
 fullnamee =document.getElementById("fullname");
 addresss =document.getElementById("address");
 errorr =document.getElementsByClassName("error");
 var flag=true;
 var correct_way = /^[A-Z a-z]+$/;

  if(addresss.value.length==0){

      addresss.style.borderColor="red";
      flag=false;
      errorr[6].innerHTML="**this field cannot be empty**";
      errorr[6].style.color="red"

   } else if(addresss.value.length>5 ){

      addresss.style.borderColor="green";
      errorr[6].innerHTML="";

   } else{

      addresss.style.borderColor="red";
      flag=false;
      errorr[6].innerHTML="**please enter full address**";
      errorr[6].style.color="red";
   }


   if(fullnamee.value.length==0){

      fullnamee.style.borderColor="red";
      flag=false;
      errorr[3].innerHTML="**this field cannot be empty**";
      errorr[3].style.color="red";


    } else if(fullnamee.value.length>5 && fullnamee.value.match(correct_way)){

      fullnamee.style.borderColor="green";
      errorr[3].innerHTML="";

    } else{

      fullnamee.style.borderColor="red";
      flag=false;
      errorr[3].innerHTML="**atleast 6 charracter and only alphabets**";
      errorr[3].style.color="red";
    } 

    if(usernamee.value.length==0){
    
       usernamee.style.borderColor="red";
       flag=false;
       errorr[0].innerHTML="**this field cannot be empty**";
       errorr[0].style.color="red";

    } else if(usernamee.value.length>2 && usernamee.value.match(correct_way)){
       
        usernamee.style.borderColor="green";
        errorr[0].innerHTML="";
       

    } else{
        
            usernamee.style.borderColor="red";
            flag=false;
            errorr[0].innerHTML="*min.3 char. only alphabets.*";
            errorr[0].style.color="red";
    }
        
    
 
    if(emaill.value.length == 0){
   
       emaill.style.borderColor="red";
       flag=false;
       errorr[5].innerHTML="**this field cannot be empty**";
       errorr[5].style.color="red";
    
    } else if((emaill.value.length <10) || (emaill.value.charAt(emaill.value.length-4)!="." && emaill.value.charAt(emaill.value.length-3)!=".")){
    
       emaill.style.borderColor="red";
       flag=false;
       errorr[5].innerHTML="**this is not a valid email address**";
       errorr[5].style.color="red";
        
    } else {
     
       emaill.style.borderColor="green";
       errorr[5].innerHTML="";
    }
   



    if(phonee.value.length == 0){
   
       phonee.style.borderColor="red";
       flag=false;
       errorr[4].innerHTML="**this field cannot be empty**";
       errorr[4].style.color="red";
   
    } else if(phonee.value.length == 10){ 
   
       phonee.style.borderColor="green";
       errorr[4].innerHTML="";
       
   
    } else {
   
     phonee.style.borderColor="red";
     flag=false;
     errorr[4].innerHTML="**not a valid number**";
     errorr[4].style.color="red";
    }  
     



    if(passwordd.value.length == 0){
    
       passwordd.style.borderColor="red";
       flag=false;
       errorr[1].innerHTML="**this field cannot be empty**";
       errorr[1].style.color="red";
    
    } else if(passwordd.value.length <5 || password.value.length >15){
   
    passwordd.style.borderColor="red";
    errorr[1].innerHTML="** range 5-15 digit **";
    errorr[1].style.color="red";
    flag=false;
   
    } else {
   
    passwordd.style.borderColor="green";
    errorr[1].innerHTML="";
   }



  if(cpasswordd.value.length == 0){
   
       cpasswordd.style.borderColor="red";
       flag=false;
       errorr[2].innerHTML="**this field cannot be empty**";
       errorr[2].style.color="red";
   
    } else if(cpasswordd.value != passwordd.value){
   
       cpasswordd.style.borderColor="red";
       flag=false;
       errorr[2].innerHTML="**your password is not matched**";
       errorr[2].style.color="red";
   
    } else {
    
       cpasswordd.style.borderColor="green";
       errorr[2].innerHTML="";
    }
     
   return flag;
}
  
 
 

    








