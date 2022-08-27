
const orbs = document.getElementById('Orbs');
const toggle = document.getElementById('toggle');
toggle.onclick = function () {
    toggle.classList.toggle('active');
    orbs.classList.toggle('active');
}