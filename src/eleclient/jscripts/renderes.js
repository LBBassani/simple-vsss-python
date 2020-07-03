
document.getElementById("test-button").addEventListener("click",get_game_info)

function get_game_info(){
    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:4002/jsonrpc"
    let request = {
        "method" : "get_game_info",
        "params" : [],
        "jsonrpc" : "2.0",
        "id" : 0,
    }
    xmlhttp.open("POST", url)
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
    xmlhttp.send(JSON.stringify(request))
    xmlhttp.onreadystatechange = function() { // Chama a função quando o estado mudar.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            update_game_info(JSON.parse(xmlhttp.response))
        }
    }

}

function update_game_info(new_info){
    console.log(new_info)
    let result = new_info["result"]
    document.getElementById("ball-x").innerHTML = result["ball"]["x"]
    document.getElementById("ball-y").innerHTML = result["ball"]["y"]
    document.getElementById("ball-speed-x").innerHTML = result["ball"]["speed_x"]
    document.getElementById("ball-speed-y").innerHTML = result["ball"]["speed_y"]

    for (let i = 0; i < 3; i++){
        let ry = result["team_yellow"][i]
        document.getElementById("y"+i+"-x").innerHTML = ry["x"]
        document.getElementById("y"+i+"-y").innerHTML = ry["y"]
        document.getElementById("y"+i+"-a").innerHTML = ry["angle"]
        document.getElementById("y"+i+"-speed-x").innerHTML = ry["speed_x"]
        document.getElementById("y"+i+"-speed-y").innerHTML = ry["speed_y"]
        document.getElementById("y"+i+"-speed-a").innerHTML = ry["speed_angle"]

        let rb = result["team_blue"][i]
        document.getElementById("b"+i+"-x").innerHTML = rb["x"]
        document.getElementById("b"+i+"-y").innerHTML = rb["y"]
        document.getElementById("b"+i+"-a").innerHTML = rb["angle"]
        document.getElementById("b"+i+"-speed-x").innerHTML = rb["speed_x"]
        document.getElementById("b"+i+"-speed-y").innerHTML = rb["speed_y"]
        document.getElementById("b"+i+"-speed-a").innerHTML = rb["speed_angle"]
    }
}