$.ajax({
  url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
  type: "GET",
  dataType: "json",
}).done((res) => {
  $("DIV#hello").text(res.hello);
});
