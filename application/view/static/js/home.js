xhr = new XMLHttpRequest();
xhr.open("GET", "/list");
xhr.send(null);
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        document.getElementById("").innerHTML = xhr.response;
    }
}
