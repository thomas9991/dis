/*function getPages(count) {
  var page_size=10;
    var modiv=count%page_size;
    pages=Math.trunc(count/page_size);    
    if(modiv>0){
      modiv=1;
    }
    pages+=modiv;

    return pages;
}
function formatearNumero(nStr) {
  nStr += '';
  x = nStr.split('.');
  x1 = x[0];
  x2 = x.length > 1 ? ',' + x[1] : '';
  var rgx = /(\d+)(\d{3})/;
  while (rgx.test(x1)) {
          x1 = x1.replace(rgx, '$1' + '.' + '$2');
  }
  return x1 + x2;
}

$(document).ready(function(){
  
  $.ajax({url: "http://localhost:8000/getProductList",  success: function(result){

       var pages = getPages(result["count"]);
    console.log(pages);



   $.each(result["results"],function(i,items){ 
    var plist = document.getElementById("productList"); 
   
    $("#productList").append('<div class="col-3 mb-5">'+result["results"][i].name+'<br>\
    <font class="text-danger"><h4 style="font-weight:lighter">$'+formatearNumero(result["results"][i].normal_price)+'</font></h1>\
    <font class="text-info">'+result["results"][i].department+'</font>\
    </div>');  
  });//each
  if(result["next"]){
    $("#products_pagination").append('<a class="page-link"><i class="fas fa-chevron-right"></i></a>');
  }
  else{
    $("#productList").append('False');
  }
   
  }});//ajax
  })





function SearchProduct() {  

  prod=document.getElementById("buscar");
  if(prod.value.length>0){
   
    
    $.ajax({url: "http://localhost:8000/getProductList?q="+prod.value,  success: function(result){
      var pages = getPages(result["count"]);
      console.log(pages);  
    var d = document.getElementById("productList");
  while (d.hasChildNodes())
  d.removeChild(d.firstChild); 
      
      $("#productList").append('<div class="col-12 mb-5"></div>'); 
  
      $.each(result["results"],function(i,items){ 
      var plist = document.getElementById("productList"); 
   
    $("#productList").append('<div class="col-3 mb-5">'+result["results"][i].name+'<br>\
    <font class="text-danger"><h4 style="font-weight:lighter">$'+formatearNumero(result["results"][i].normal_price)+'</font></h1>\
    <font class="text-info">'+result["results"][i].department+'</font>\
    </div>'); 
     
  
        
        
      //$("#productList").append(result[i].category+' '+result[i].product_name+' '+result[i].product_price+'<img src="'+result[i].product_image+'">'); 
   
  });
  if(result["next"]){
    $("#products_pagination").append('<a class="page-link"><i class="fas fa-chevron-right"></i></a><span id="urlr" style="display:none">'+result["next"]+'</span>');
    var nexturl = document.getElementById("urlr"); 
    alert(nexturl.value);
  }
  else{
    $("#productList").append('False');
  }
  }});

  }
  else{
    alert("fail");
  }
 
}
function SearchProductHomePage() { 
  location.href="http://localhost:8000/Productos";




 }


//Enter
 const input = document.querySelector('#buscar');
 prod=document.getElementById("buscar");
 input.addEventListener('keyup',function(e){
     if (e.keyCode === 13) {
      $.ajax({url: "http://localhost:8000/getProductList?q="+prod.value,  success: function(result){
        var d = document.getElementById("productList");
    while (d.hasChildNodes())
    d.removeChild(d.firstChild); 
        
        $("#productList").append('<div class="col-12 mb-5"></div>'); 
    
        $.each(result["results"],function(i,items){ 
          var plist = document.getElementById("productList"); 
       
        $("#productList").append('<div class="col-3 mb-5">'+result["results"][i].name+'<br>\
        <font class="text-danger"><h4 style="font-weight:lighter">$'+formatearNumero(result["results"][i].normal_price)+'</font></h1>\
        <font class="text-info">'+result["results"][i].department+'</font>\
        </div>'); 

      });
    }});
   }  
 });
*/