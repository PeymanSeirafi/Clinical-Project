/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./project_statics/admin-panel/js/**/*.js",
    "./project_statics/js/**/*.js",
    "./project_statics/npm-files/node_modules/flowbite/**/*.js",
    "./main/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  // plugins: [require("flowbite/plugin")],
};

// npx tailwindcss -i ./project_statics/css/input.css -o ./project_statics/css/output.css --watch
