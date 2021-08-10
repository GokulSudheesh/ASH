let current_theme = "Coral";
const themes = {"Coral": ["coral", "wheat", "white", "black", "black", "white"], 
                "Ocean": ["#004084", "#75b8ff","#0e59e5", "white", "#133455", "white"], 
                "Starlight" : ["#3e2779", "#b9a2f5", "#a044d5", "white", "#413269", "white"]};

function reply(message){
    $.get("/get", {data : message}, function(response){
        $(".container").append("<div class=\"ai\"><div class=\"ai-textbox ai-textbox-"+current_theme+"\">"+response+"</div></div>");
        $(".container").scrollTop(parseInt($(".container")[0].scrollHeight));
    });
}

$("#send-button").on("click", function(){
    let message = $("#message-box").val();    
    if(message != ""){
        //console.log(message);
        $(".container").append("<div class=\"user\"><div class=\"user-textbox user-textbox-"+current_theme+"\">"+message+"</div></div>");
        $(".container").scrollTop(parseInt($(".container")[0].scrollHeight));
        $("#message-box").val("");
        reply(message);
    }
});

$("#message-box").keypress(function(event){
    if (event.key == "Enter"){
        $("#send-button").click();
    }    
});

$(".theme").on("click", function(){
    let id = this.getAttribute("id");
    if (id != current_theme){
        $("#"+current_theme).removeClass("theme-select");
        $("#"+id).addClass("theme-select");
        /// Change the css properties
        $(".container").css("background-color", themes[id][0]);
        $("#send-button").css("background-color", themes[id][0]);
        $("body").css("background-color", themes[id][1]);
        $(".user-textbox").css("background-color", themes[id][2]);
        $(".user-textbox").css("color", themes[id][3]);
        $(".ai-textbox").css("background-color", themes[id][4]);
        $(".ai-textbox").css("color", themes[id][5]);
        current_theme = id;
    }
});