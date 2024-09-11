// File: tailwind.config.js
// Requires: It watches the ./src folder for changes.

/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/**/*.{html,js}"],
    theme: {
        extend: {
            spacing: {
                '128': '32rem',
                '144': '36rem',
            },
            borderRadius: {
                '4xl': '2rem',
            }
        },
        container: {
            center: true,
        },
        screens: {
            sm: '480px',
            md: '768px',
            lg: '976px',
            xl: '1440px',
        },
        fontFamily: {
            sans: ['Hind', 'sans-serif'],
            serif: ['Merriweather', 'serif'],
        }
    },
    plugins: [],
}

