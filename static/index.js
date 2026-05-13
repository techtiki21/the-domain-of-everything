themeToggle = document.getElementById("theme-toggle")
body = document.querySelector("body")
lightTheme = true

themeToggle.addEventListener("click", function(){
    if (lightTheme == true){
        body.style.background = "linear-gradient(to bottom, gray 0%, black 100%) no-repeat fixed"
        body.style.color = "white"
        body.style.setProperty("--text-outline-rgb", "0, 0, 0")
        themeToggle.innerText = "Light Mode"
        lightTheme = false
    }
    else{
        body.style.background = "linear-gradient(to bottom, white 0%, gray 100%) no-repeat fixed"
        body.style.color = "black"
        body.style.setProperty("--text-outline-rgb", "255, 255, 255")
        themeToggle.innerText = "Dark Mode"
        lightTheme = true
    }
})