$(document).ready(() => {
  $('INPUT#language_code').keypress((key) => {
    if (key.keyCode === 13) {
      const code = $('INPUT#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + code, (res) => {
        $('DIV#hello').text(res.hello);
      });
    }
  });
});
