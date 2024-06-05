module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {

      colors: {
        'dark-bg': '#242424',
        'dark-text': '#e5e5e5',
        'dark-text-disable': '#999999',
        'dark-card': '#333333',
        'dark-card-hover': '#444444',
        'dark-card-active': '#555555',
        'dark-primary': '#5DEBD7',
        'dark-container': '#3a3a3a',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0, transform: 'scale(0.95)' },
          '100%': { opacity: 1, transform: 'scale(1)' },
        },
        fadeOut: {
          '0%': { opacity: 1, transform: 'scale(1)' },
          '100%': { opacity: 0, transform: 'scale(0.95)' },
        },
        scaleInTop: {
          '0%': { opacity: 0, transform: 'scale(0) translate(50%, 50%)' },
          '100%': { opacity: 1, transform: 'scale(1) translate(0, 0)' },
        },
        scaleOutTop: {
          '0%': { opacity: 1, transform: 'scale(1) translate(0, 0)' },
          '100%': { opacity: 0, transform: 'scale(0) translate(50%, 50%)' },
        },
        scaleInBottom: {
          '0%': { opacity: 0, transform: 'scale(0) translate(50%, -50%)' },
          '100%': { opacity: 1, transform: 'scale(1) translate(0, 0)' },
        },
        scaleOutBottom: {
          '0%': { opacity: 1, transform: 'scale(1) translate(0, 0)' },
          '100%': { opacity: 0, transform: 'scale(0) translate(50%, -50%)' },
        },
        'slide-in': {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(0)' },
        },
        'slide-out': {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-100%)' },
        },
        'slide-rl-in': {
          '0%': { transform: 'translateX(100%)' },
          '100%': { transform: 'translateX(0)' },
        },
        'slide-rl-out': {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(100%)' },
        },
      },
      animation: {
        fadeIn: 'fadeIn 0.2s ease-out forwards',
        fadeOut: 'fadeOut 0.2s ease-out forwards',
        scaleIn: 'scaleIn 0.3s ease-out forwards',
        scaleOut: 'scaleOut 0.3s ease-out forwards',
        'slide-in': 'slide-in 0.5s ease-out',
        'slide-out': 'slide-out 0.5s ease-out',
        'slide-rl-out': 'slide-rl-out 0.5s ease-out',
        'slide-rl-in': 'slide-rl-in 0.5s ease-out',
      }

    },
  },
  plugins: [
    require('tailwind-scrollbar'),
  ],
}