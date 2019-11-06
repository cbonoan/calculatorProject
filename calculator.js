//display
function dis(val)
{
    var input = document.getElementById(val).value;
    document.getElementById("output").value+=input;
}
//clear
function cl(){
    document.getElementById("output").value="";
}

function cancel(){
    var str = document.getElementById("output").value;
    str = str.slice(0,str.length-1)
    document.getElementById("output").value = str;
}