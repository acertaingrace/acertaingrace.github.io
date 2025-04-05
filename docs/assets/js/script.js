/* shoutout to GDSC USYD 2023 workshop */
/* ~~~~~~~~~~~ Menu ~~~~~~~~~~~~~~ */

/*selects the new set of hyperlinks that we would like to show once the hamburger button is pressed*/
const menu = document.querySelector(".menu");
/*selects each menu items*/
const menuItems = document.querySelectorAll(".menuItem");
/*selects the button with class name "hamburger"*/
const hamburger= document.querySelector(".hamburger");
/*selects the i tag containing our icon*/
const menuButton= document.querySelector(".menuButton");

const toggleMenu = () => {
  if (menu.classList.contains("showMenu")) {
     menu.classList.remove("showMenu");
     menuButton.innerHTML = "menu";
   } else {
     menu.classList.add("showMenu");
     menuButton.innerHTML = "close";
   }
}

hamburger.addEventListener("click", toggleMenu);

menuItems.forEach( 
 function(menuItem) { 
   menuItem.addEventListener("click", toggleMenu);
 }
)
