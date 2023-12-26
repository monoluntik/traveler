function showSection(sectionNumber) {
    var sections = document.getElementsByClassName('section');
    for (var i = 0; i < sections.length; i++) {
      sections[i].classList.remove('active');
    }
  
    var selectedSection = document.getElementById('section' + sectionNumber);
    selectedSection.classList.add('active');
  
    var buttons = document.getElementsByTagName('button');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].classList.remove('active');
    }
  
    var selectedButton = document.querySelector('button[data-section="' + sectionNumber + '"]');
    selectedButton.classList.add('active');
  }
  