
var axios = require("axios")

document.getElementById("info-button").addEventListener("click",get_game_info)
document.getElementById("move-button").addEventListener("click", () => {
    document.getElementById("r1-vel1").disabled = true
    document.getElementById("r1-vel2").disabled = true
    document.getElementById("r2-vel1").disabled = true
    document.getElementById("r2-vel2").disabled = true
    document.getElementById("r3-vel1").disabled = true
    document.getElementById("r3-vel2").disabled = true
    document.getElementById("move-button").disabled = true

    move_team(
        [
            [parseFloat(document.getElementById("r1-vel1").value), parseFloat(document.getElementById("r1-vel2").value)],
            [parseFloat(document.getElementById("r2-vel1").value), parseFloat(document.getElementById("r2-vel2").value)],
            [parseFloat(document.getElementById("r3-vel1").value), parseFloat(document.getElementById("r3-vel2").value)]
        ]
    )
} )


function get_game_info(){
    var url = "http://localhost:4002/jsonrpc"
    let request = {
        "method" : "get_game_info",
        "params" : [],
        "jsonrpc" : "2.0",
        "id" : 0,
    }
    
    axios.post(url, request).then(
        function(response){
            update_game_info(response["data"]["result"])
        }
    )

}

function move_team(velocidades){
    var url = "http://localhost:4002/jsonrpc"
    let request = {
        "method" : "move_team",
        "params" : [velocidades],
        "jsonrpc" : "2.0",
        "id" : 0,
    }
    console.log(request)

    axios.post(url, request).then( (_) => {
        document.getElementById("r1-vel1").disabled = false
        document.getElementById("r1-vel2").disabled = false
        document.getElementById("r2-vel1").disabled = false
        document.getElementById("r2-vel2").disabled = false
        document.getElementById("r3-vel1").disabled = false
        document.getElementById("r3-vel2").disabled = false
        document.getElementById("move-button").disabled = false
    } )
}

function update_game_info(result){
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