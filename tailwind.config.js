/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        accent: {
          50: '#f5f7ff',
          100: '#e6eaff',
          500: '#4f46e5',
          600: '#4338ca'
        }
      }
    },
  },
  plugins: [],
};
