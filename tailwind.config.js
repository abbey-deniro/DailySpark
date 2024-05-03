/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
      },
      colors: {
        'bg-pink': '#eeaeca',
        'bg-blue': '#94bbe9',
      },
      fontFamily: {
        'playfair': ['"PlayFair Display"', "sans-serif"],
      }
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}

