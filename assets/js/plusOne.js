// const checkBox = document.getElementById("plusOne");

// checkBox.addEventListener("click", () => {
//   const boxes = document.getElementsByClassName("plusOne");

//   for (const box of boxes) {
//     // 👇️ hides element
//     // box.style.visibility = "hidden";

//     // 👇️ removes element from DOM
//     box.style.display = "block";
//   }
// });

function myFunction() {
  let checkBox = document.getElementById("plusOne");
  let pog = document.getElementById("plusOneGuest");
  let pfn = document.getElementById("plusOneFirstName");
  let pln = document.getElementById("plusOneLastName");
  let pfc = document.getElementById("plusOneFoodChoice");
  if (checkBox.checked == true) {
    pog.style.display = "block";
    pfn.style.display = "block";
    pln.style.display = "block";
    pfc.style.display = "block";
  } else {
    pog.style.display = "none";
    pfn.style.display = "none";
    pln.style.display = "none";
    pfc.style.display = "none";
  }
}
