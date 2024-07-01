$(".edit_button").on("click", function (event) {
  let data = document.getElementById(
      `card_${event.target.id.split("_")[2]}`
  ).children;

  let name_field = document.getElementById("old-name");
  let description_field = document.getElementById("old-description");
  let prev_photo = document.getElementById("prev_photo");

  name_field.value = data[0].innerHTML;
  description_field.value = data[1].innerHTML;
  prev_photo.src = `/static/admin-panel/assets/services/${event.target.id.split("_")[2]}.png`;
});
