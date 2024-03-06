function submit_entry(){
    var item = document.getElementById("recipetitle");
    var item = document.getElementById("recipetitle");
    var itemx = document.getElementById("meal");
    var item2 = itemx.options[itemx.selectedIndex].text;
    var item3 = document.getElementById("cuisine");
    var item4 = document.getElementById("ingredients");
    var item5 = document.getElementById("description");
    var item6 = document.getElementById("directions");
    
    var entry = {
       'items' : item.value,
       'items2':item2,
       'items3' : item3.value,
       'items4' : item4.value,
       'items5' : item5.value,
       'items6' : item6.value,
       
       
    };
   
    fetch('http://127.0.0.1:5000/addrecipe' ,
    {
      method: "POST",
      cridentials: "include",
      body: JSON.stringify(entry),
      cashe: "no-cache",
      headers: {
        'Content-type': 'application/json',
        'Accept': 'application/json'
        
      }
     
    })
    .then(function(response){
      if(response.status !== 200 ){
        console.log(`RESPONSE NOT 200: ${reponse.status}`);
        return ;
      }
      response.json().then((data) => 
        console.log(data)
      );
    })
  }