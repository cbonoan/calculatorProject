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

function neg(){
    var expression = document.getElementById("output").value;
    if(!expression.includes("-")){
        var newExp = "-"+document.getElementById("output").value
        document.getElementById("output").value = newExp
    }
    else{
        var newExp = expression.slice(1);
        document.getElementById("output").value = newExp;
    }
    
}

function calc(){
    var err = "Invalid Expression"
    if(document.getElementById("output").value != ""){
        try{
            var expression = document.getElementById("output").value;
            document.getElementById("output").value = eval(expression);
        }
        catch(SyntaxError){
            document.getElementById("output").value = err;
        }
    }
    else{
        document.getElementById("output").value = ""
    }
}