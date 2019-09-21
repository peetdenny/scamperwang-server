urlBase='/'
classesURL = urlBase+'classes'
postURL = urlBase+"upload"

var form = document.getElementById('form');
form.onsubmit = function() {
  var fileInput = document.getElementById('file');
  var file = fileInput.files[0];
  var formData = new FormData();
  formData.append('file', file);

  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var data = JSON.parse(this.response)
    var perc = parseFloat(data['confidence']) * 100;
    resp = `We're ${perc}% sure that this is a ${data['prediction']}`
    console.log(resp)
    document.getElementById("result").innerText=resp
  }
  xhr.open('POST', postURL, true);
  xhr.send(formData);
  return false;
}