  
  var selectAll = document.getElementById("selectAll")
  selectAll.addEventListener( 'change', function() {
    toggle(this)
  });
  
  function filterFunction() {
    var input, filter, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByClassName("checkbox")
    
    for (i = 0; i < a.length; i++) {
      var lab = a[i].getElementsByTagName("label")[0]
      txtValue = lab.textContent || lab.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }

  function toggle(source) {
    checkboxes = document.getElementsByName('cities');
    for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = source.checked;
    }
  }

  function getCheckedBoxes(chkboxName) {
    var checkboxes = document.getElementsByName(chkboxName);
    var checkboxesChecked = [];
    // loop over them all
    for (var i=0; i<checkboxes.length; i++) {
       // And stick the checked ones onto an array...
       if (checkboxes[i].checked) {
          checkboxesChecked.push(checkboxes[i]);
       }
    }
    // Return the array if it is non-empty, or null
    return checkboxesChecked.length > 0 ? checkboxesChecked : null;
  }

  var download_btn = document.getElementsByClassName("bottombtn")[0]
  var temp = 1
  var temp_count = 0

  function download(){
    var checkedBoxes = getCheckedBoxes("cities");
    if (!checkedBoxes){
      alert("Please Select Cities First")
      return null;
    }
    temp_count = checkedBoxes.length
    download_btn.style.display = "none";
    open_modal()
    for (var i=0; i<checkedBoxes.length; i++) {
      console.log(checkedBoxes[i].id)
      fetch_request(checkedBoxes[i].id)
    }
  }

  function fetch_request(city){
    var base_url = window.location.origin
    fetch(base_url+'/city/'+city).then( (res) => {
      return res.json();
    }).then((addresses) => {
      download_csv(addresses['addresses'], city);
      if (temp_count == temp++){
        close_modal();
        download_btn.style.display = "block";
      }
    }).catch((error) => {
      console.log(error)
      if (temp_count == temp++){
        close_modal();
        download_btn.style.display = "block";
      }
    });
  }

  // Get the modal
var modal = document.getElementById('myModal');

// Get the main container and the body
var body = document.getElementsByTagName('body');
var container = document.getElementById('myContainer');

// Open the modal
function open_modal() {
    modal.className = "Modal is-visuallyHidden";
    setTimeout(function() {
      container.className = "MainContainer is-blurred";
      modal.className = "Modal";
    }, 100);
    container.parentElement.className = "ModalOpen";
}

// Close the modal
function close_modal() {
  modal.className = "Modal is-hidden";
  body.className = "";
  container.className = "MainContainer";
  container.parentElement.className = "";
}