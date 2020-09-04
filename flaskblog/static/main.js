// whole modal section with display: none at first
const modal = document.querySelector('#my-modal');
// Button "delete" it will trigger to open modal section
const modalBtn = document.querySelector('#modal-btn');
const closeBtn = document.querySelector('.close');
const keepItBtn = document.querySelector('#modal-keepit');

// triggers function which opens modal window
modalBtn.addEventListener('click', openModal);
// triggers function which closes modal by pressing X button
closeBtn.addEventListener('click', closeModal);
// trigers function which closes modal by pressing "Keep it" button
keepItBtn.addEventListener('click', closeModal);

window.addEventListener('click', outsideClick);

function openModal() {
  modal.style.display = 'block';
}

function closeModal() {
  modal.style.display = 'none';
}

function outsideClick(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}
