$(document).ready(function(){
    $.ajax({url: "http://localhost:8000/getContactsAPIView",  success: function(result){
      /*  $("#contactsList").append('<div class="row"> <div id="contactsb" class="col-12 text-secondary text-center">\
        \
         </div> </div>');*/
          
      
        $("#contactsList").append('<table class="table   border" id="contacts">\
          <tr class="table-dark" style="opacity:1" >\
              <td><h4 style="font-weight:lighter;letter-spacing:2px">CARGO</h4></td>\
              <td><h4 style="font-weight:lighter;letter-spacing:2px">NOMBRE</h4></td>\
              <td><h4 style="font-weight:lighter;letter-spacing:2px">CORREO</h4></td>\
              <td><h4 style="font-weight:lighter;letter-spacing:2px">NUMERO</h4></td>\
          </tr>'); 
    
      $.each(result,function(i,items){
          var role =result[i].role.toUpperCase();
          
          if(result[i].first_name && result[i].last_name){          
          var name = (result[i].first_name+ ' '+result[i].last_name).toUpperCase();
          }
          else{
          var name = '';
          }

          var email = result[i].email.toUpperCase();
          if(result[i].phone){
          var phone = result[i].phone;
          }
          else{
        var phone = ' ';
        
        
          }
          
        $("#contacts").append('<tr class="text-dark">\
            <td >'+role+'</td>\
            <td>'+name+'</td>\
            <td>'+email+'</td>\
            <td>'+phone+'</td>\
        </tr>'); 
        /*
        $("#contactsb").append(role+' - \
            '+name+' - \
            '+email+' - \
            '+phone+'<hr>');          
           */
         
         



    });
    }});
    })