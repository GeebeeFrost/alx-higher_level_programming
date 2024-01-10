$(document).ready(() => {
  $("INPUT#btn_translate").click(() => {
    const code = $("INPUT#language_code").val();
    $.get("https://hellosalut.stefanbohacek.dev/?lang=" + code, (res) => {
      $("DIV#hello").text(res.hello);
    });
  });
});
