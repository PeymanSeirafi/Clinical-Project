$(".edit_button").on('click', function (event) {
  let data = document.getElementById(
    `card_${event.target.id.split("_")[2]}`
  ).children;

  let username = document.getElementById("old-username");
  let password = document.getElementById("old-password");

  username.value = data[0].children[0].innerHTML;
  password.value = data[1].children[0].innerHTML;
})