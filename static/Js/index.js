
// lucide icons 
lucide.createIcons();

//Aos animation
AOS.init({
  once: true,
}); 


/// header banner sizee 
var clientHeight = document.documentElement.clientHeight;
const headers = document.querySelectorAll('.header')
headers.forEach(header => (
  header.style.height = clientHeight + 'px'
))


let year = document.querySelector('.footer-year')
year.textContent = new Date().getFullYear()


const nav = document.querySelector('.nav-hover'),
  navContacts = document.querySelector('.nav-contacts'),
  navLang = document.querySelector('.nav-lang'),
  navLists = document.querySelector('.nav-lists')
 navBg = document.querySelector('.nav-bg')

if (nav !== null)  {

window.addEventListener('scroll', () => {
  if (window.scrollY > 1 ) {
    dropdownItems.classList.remove('grid-rows-[1fr]', 'border-[0.5px]')
    nav.classList.add('bg-white', 'border-blue', 'nav-active')
    navContacts.classList.add('text-blue')
    navLang.classList.remove('text-white')
    navLang.classList.add('text-dark')
    navLists.classList.remove('text-white')
    navLists.classList.add('text-dark')
    navLang.querySelector('.vector').classList.remove('bg-white')
    navLang.querySelector('.vector').classList.add('bg-dark')

  }
  else {
    nav.classList.remove('bg-white', 'border-blue', 'nav-active')
    navContacts.classList.remove('text-blue')
    navLang.classList.remove('text-dark')
    navLang.classList.add('text-white')
    navLists.classList.remove('text-dark')
    navLists.classList.add('text-white')
    navLang.querySelector('.vector').classList.remove('bg-dark')
    navLang.querySelector('.vector').classList.add('bg-white')

  }
})
}



const navDropdown = document.querySelector('.nav-dropdown'),
  dropdownItems = document.querySelector('.dropdown-item')

if (window.scrollY > 1 ) {
  dropdownItems.classList.remove('grid-rows-[1fr]', 'border-[0.5px]')
}
navDropdown.addEventListener('click', (e) => {
  e.stopPropagation()
  console.log(1);
  dropdownItems.classList.toggle('grid-rows-[1fr]')
  dropdownItems.classList.toggle('border-[0.5px]')

})
const navBurger = document.querySelector('.navbar-burger')
const navClose = document.querySelector('.nav-close')

navBurger.addEventListener('click', () => {
  navLists.classList.add("!right-0")
  document.body.classList.add("overflow-hidden")
  navBg.classList.remove('hidden')
})
navClose.addEventListener('click', () => {
  navLists.classList.remove("!right-0")
  document.body.classList.remove("overflow-hidden")
  navBg.classList.add('hidden')
})
navBg.addEventListener('click', () => {
  navLists.classList.remove("!right-0")
  document.body.classList.remove("overflow-hidden")
  navBg.classList.add('hidden')
})

const navSearch = document.querySelector(".nav-search")
const   searchPanel  =  document.querySelector('.search-panel')


navSearch.addEventListener('click', () => {
  searchPanel.classList.toggle('!bottom-0')
  document.body.classList.toggle("overflow-hidden")
})
