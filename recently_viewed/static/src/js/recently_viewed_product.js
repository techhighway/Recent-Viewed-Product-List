/* Add Product To Recently Viwed Product List*/

function recent_product_viewed() {
	var url = window.location.href;
	if(url.indexOf('/shop/product/') != -1){
	    //console.log("create post is working!");
		var product_id = document.getElementsByName("product_id_new")[0].value;
		if (product_id==0){
			return false;
		}
	    $.ajax({
		url : "/shop/add_product_to_recently_viewed", 
			data: { product_id: product_id},
		success : function(data) {
		},
		error : function() {
		}
	    });
    }
};
recent_product_viewed();

// TO INHERIT PRODUCT MENU TO RELOAD PAGE FOR RECENT PRODUCT LIST
function redirect_to_shop(){
  window.location.replace("/shop");
}
