/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html, js}"],
  theme: {
    extend: {},
  },
  // plugins: [require("flowbite/plugin")],
};

// npx tailwindcss -i ./static_files/project_statics/css/input.css -o ./static_files/project_statics/css/output.css --watch
