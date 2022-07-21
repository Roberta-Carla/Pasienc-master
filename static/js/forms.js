// window.myFunction = function validationEvent(){
//     var fabstract = document.forms["myForm"]["message"].value;
//     var fcategories = document.forms["myForm"]["categories"].value; 

//     if (fabstract != '')
//         {
//             alert("Abstract has done on OnSubmit event!!");
//             return true;
//         }
//     else{
//         alert("Abstract cannot be blind !!!");
//         return false;
//     }

// }

function validationForm(form)
{
  if(! form.call_paper.value ) {
     alert("Error: The abstract is empty");
     //form.fieldname.focus();
     return false;
  }
  return true;
}