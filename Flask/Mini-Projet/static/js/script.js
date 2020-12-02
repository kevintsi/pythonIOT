console.log("test")
window.onload = () => {
    document.getElementById("hotelSearch").oninput = async (e) => {
        console.log("value change "+e.target.value)
        var boxResultSearch;
        if(document.getElementById("boxResultSearch") != null){
            while (document.getElementById("boxResultSearch").firstChild) {    document.getElementById("boxResultSearch").removeChild(document.getElementById("boxResultSearch").firstChild);}
            try { 
                response = await fetch("/hotel/name/"+e.target.value)
                data = await response.json()
                var ul = document.createElement("ul")
                data.forEach((hotel) => {
                    var li = document.createElement("li")
                    var a = document.createElement("a")
                    a.innerHTML = hotel.name
                    a.href = "/hotel/"+hotel.id
                    li.appendChild(a)
                    ul.appendChild(li)
                })
            } catch (error) {
                console.log(error)
            }
            document.getElementById("boxResultSearch").appendChild(ul)
        }else {
            boxResultSearch = document.createElement("div")
            boxResultSearch.id = "boxResultSearch"
            document.getElementById("searchInputBox").appendChild(boxResultSearch)
        }

    }
}