function getproducts(a,b)
{
	// alert(a);
	// alert(b);
var elements=document.getElementsByClassName("category");
 for(var i=0;i<elements.length;i++)
 {
 if((elements[i].value)!=b)
 {
  elements[i].checked="";
 }
 }
$.ajax({
              url: '/user/finds/', 
              data:
              {
                     
                  'val':b
                    
                },

                
                success: function (data) 
                  {
                    alert(data);
                    alert(document.getElementById("contents"));
                    // $("#fee").val(data);
                    document.getElementById("contents").innerHTML=data;

                    
                } 
              }); 



}
function totp(q)
{
  // alert(q.value);
  var quantity=$("#quantity").val();
  // alert(quantity);
  var price=$("#price").val();
  // alert(price);
  total=quantity*price;
  // alert(total);
  $("#tprice").val(total);
// $.ajax({
//               url: '/user/total/', 
//               data:
//               {
                     
//                  'valu':quantity,'pric':price,
                    
//               },
//               success: function (data) 
//                 {
//                   alert(data);
//                   $("#tprice").val(data);
                   
//                 }
                   
//       });
}      