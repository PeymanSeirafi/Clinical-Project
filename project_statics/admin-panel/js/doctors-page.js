$(".edit_button").on('click', function (event) {
  let data = document.getElementById(`card_${event.target.id.split("_")[2]}`).children;

  let name_field = document.getElementById("old-name");
  let career_field = document.getElementById("old-career");
  let description_field = document.getElementById("old-description");
  let prev_photo = document.getElementById("prev_photo");

  name_field.value = data[1].innerHTML;
  career_field.value = data[2].innerHTML;
  description_field.value = data[3].innerHTML;
  prev_photo.src = data[0].src;
})