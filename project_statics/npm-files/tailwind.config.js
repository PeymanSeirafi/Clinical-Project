/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../admin-panel/js/**/*.js",
    "../js/**/*.js",
    "./node_modules/flowbite/**/*.js",
    "../../main/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};

// npx tailwindcss -i ../css/input.css -o ../css/output.css --watch