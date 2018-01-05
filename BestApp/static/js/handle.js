
function getActivitiesFromOutput(output_id) {

    var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            {
                //callback(xmlHttp.responseText);
                element = document.getElementById('output_' + output_id);
                element.innerHTML = xmlHttp.responseText;
                }
        };
    xmlHttp.open("GET", "/BestApp/activities_list/"+ output_id + "/", true); // true for asynchronous
    xmlHttp.send(null);
}
function load(){
// init EventListener
    console.log("load() is called");
    {% for output in outputs %}
    $(document).getElementById("{{"output_"|add:""}}{{output.id}}").addEventListener("click",get_activities({{output.id}}));
    {% endfor %}
    console.log("load() End");
}
