themeToggle = document.getElementById("theme-toggle")
body = document.querySelector("body")
lightTheme = true

themeToggle.addEventListener("click", function(){
    if (lightTheme == true){
        body.style.background = "linear-gradient(to bottom, white 100%, gray 0%) no-repeat fixed"
        themeToggle.innerText = "Light Mode"
    }
})