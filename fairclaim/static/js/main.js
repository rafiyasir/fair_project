const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#messages').fadeOut('slow');
}, 3000)

//for type effect
class TypeWriter {
    constructor(txtElement, words, wait = 3000) {
      this.txtElement = txtElement;
      this.words = words;
      this.txt = '';
      this.wordIndex = 0;
      this.wait = parseInt(wait, 10);
      this.type();
      this.isDeleting = false;
    }
  
    type() {
      // Current index of word
      const current = this.wordIndex % this.words.length;
      // Get full text of current word
      const fullTxt = this.words[current];
  
      // Check if deleting
      if(this.isDeleting) {
        // Remove char
        this.txt = fullTxt.substring(0, this.txt.length - 1);
      } else {
        // Add char
        this.txt = fullTxt.substring(0, this.txt.length + 1);
      }
  
      // Insert txt into element
      this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;
  
      // Initial Type Speed
      let typeSpeed = 180;
  
      if(this.isDeleting) {
        typeSpeed /= 2;
      }
  
      // If word is complete
      if(!this.isDeleting && this.txt === fullTxt) {
        // Make pause at end
        typeSpeed = this.wait;
        // Set delete to true
        this.isDeleting = true;
      } else if(this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        // Move to next word
        this.wordIndex++;
        // Pause before start typing
        typeSpeed = 500;
      }
  
      setTimeout(() => this.type(), typeSpeed);
    }
  }
  
  
  // Init On DOM Load
  document.addEventListener('DOMContentLoaded', init);
  
  // Init App
  function init() {
    const txtElement = document.querySelector('.txt-type');
    const words = JSON.parse(txtElement.getAttribute('data-words'));
    const wait = txtElement.getAttribute('data-wait');
    // Init TypeWriter
    new TypeWriter(txtElement, words, wait);
  }

  function altEmail(){
    const email = document.querySelector('.alt-email');
    if(email.className === 'fas fa-envelope-open custom-color alt-email')
      email.className = 'fas fa-envelope-open-text custom-color alt-email';
    else if(email.className === 'fas fa-envelope-open-text custom-color alt-email')
      email.className = 'fas fa-envelope custom-color alt-email';
    else
      email.className = 'fas fa-envelope-open custom-color alt-email';
  }

  function altPhone() {
    const phone0 = document.getElementById('phone-0');
    const phone1 = document.getElementById('phone-1');
    const phone2 = document.getElementById('phone-2');
    const phone3 = document.getElementById('phone-3');
    const phone4 = document.getElementById('phone-4');
    if(phone0.className === ''){
      phone0.className = 'd-none';
      phone1.className = '';
    }
    else if(phone1.className === ''){
      phone1.className = 'd-none';
      phone2.className = '';
    }
    else if(phone2.className === ''){
      phone2.className = 'd-none';
      phone3.className = '';
    }
    else if(phone3.className === ''){
      phone3.className = 'd-none';
      phone4.className = '';
    }
    else if(phone4.className === ''){
      phone4.className = 'd-none';
      phone0.className = '';
    }
  }
  setInterval(() => altPhone(), 1000);
  setInterval(() => altEmail(), 1000);