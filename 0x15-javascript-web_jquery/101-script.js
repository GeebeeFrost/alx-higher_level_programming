$(document).ready(() => {
  $("DIV#add_item").click(() => {
    $("<li>").text("Item").appendTo("UL.my_list");
  });
  $("DIV#remove_item").click(() => {
    $("UL.my_list li:last-child").remove();
  });
  $("DIV#clear_list").click(() => {
    $("UL.my_list li").remove();
  });
});
