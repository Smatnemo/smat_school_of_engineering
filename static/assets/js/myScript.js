function myFunction(x) {
    x.classList.toggle("change");
    if (document.getElementById("mySidenav").style.width == "250px") {
      document.getElementById("mySidenav").style.width = "0";
      document.getElementById("mySidenav1").style.width = "0";
      document.getElementById("mySidenav2").style.width = "0";
      document.getElementById("mySidenav3").style.width = "0";
      document.getElementById("mySidenav4").style.width = "0";
      document.getElementById("mySidenav5").style.width = "0";
      document.getElementById("mySidenav6").style.width = "0";
      document.getElementById("myrightside").style.marginLeft = "0";
      document.getElementById("myrightside").style.marginRight = "0";
      document.getElementById("lessonContainer").style.marginRight = "0";
    } else {
      document.getElementById("mySidenav").style.width = "250px";
      document.getElementById("myrightside").style.marginLeft = "250px";
      document.getElementById("myrightside").style.marginRight = "-250px";
      document.getElementById("lessonContainer").style.marginRight = "-250px";
    }
  //   document.getElementById("mySidenav").style.width = "250px";
  //   ocument.getElementById("myrightside").style.marginLeft = "250px";
  }

  function openNav(x) {
      document.getElementById(x).style.width = "250px";
      // document.getElementById("myrightside").style.marginLeft = "250px";
  }


  function closeNav(x) {
    document.getElementById(x).style.width = "0";
    // document.getElementById("myrightside").style.marginLeft = "0";
}

function openmenuitems(n, cc){
    var x = document.getElementsByClassName("menulinks")[n-1];
    var y = x.cloneNode(true);
    y.setAttribute("style", "height:auto; visibility: hidden;");
    x.parentNode.appendChild(y);
    var height = w3_getStyleValue(y, "height");
    x.setAttribute("style", "height:" + height);
    x.parentNode.removeChild(y);
    if (!cc && w3_getStyleValue(x, "height") == height) { 
        x.style.height = "0"; 
        x.style.visibility = "hidden";
    } else { 
        closemenuitems();
        x.style.height = height;
        x.style.visibility = "visible";
    }
    // var x = document.getElementsByClassName("menulinks")[n-1];
    // if (x.style.height == "none") {
    //     x.style.display = "block";
    // } else {
    //     x.style.display = "none";
    // }

}

function closemenuitems() {
    var i, x = document.getElementsByClassName("menulinks"), l = x.length;
    for (i = 0; i <l; i++) {
        x[i].style.height = "0";
        x[i].style.visibility = "hidden";
    }
}

openmenuitems(exActiveNo, true);

function w3_getStyleValue(elmnt,style) {
    if (window.getComputedStyle) {
        return window.getComputedStyle(elmnt,null).getPropertyValue(style);
    } else {
        return elmnt.currentStyle[style];
    }
}

function openclose(x, y) {
    x.classList.toggle("change");
    if (document.getElementById(y).style.width == "250px") {
        document.getElementById(y).style.width = "0";
        ocument.getElementById("myrightside").style.marginLeft = "0";
        document.getElementById("myrightside").style.marginRight = "0";
    } else {
        document.getElementById(y).style.width = "250px";
        document.getElementById("myrightside").style.marginLeft = "250px";
        document.getElementById("myrightside").style.marginRight = "-250px";
    }
}