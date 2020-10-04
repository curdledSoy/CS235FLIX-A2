let coll = document.getElementsByClassName("genres-drop-down");
let i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    const content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}


function change_nav(){
  if(document.getElementById("nav").style.display === 'flex'){
      document.getElementById('content-2').style.marginLeft = '0px'
      document.getElementById("nav").style.display = 'none';
    }
    else {
      document.getElementById('content-2').style.marginLeft = '200px'
      document.getElementById("nav").style.display = 'flex';
    }
}



$(".chosen-select").chosen({width: "100%"});




