var count = 0;
function add_thing(){
    var num = document.getElementById("1").value;
    for(var i = 0; i < num; i++){
        var target = document.getElementById("list");
        var item = '<li onclick = self_del(this) id ='+count+' >　</li>';
        target.insertAdjacentHTML("beforeend", item);
        count += 1;
    }
}

function self_del(item){
    item.remove()
}