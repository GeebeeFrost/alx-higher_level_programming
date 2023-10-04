$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json'
}).done((res) => {
  $('DIV#hello').text(res.hello);
});
