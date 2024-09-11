# File: tailwind-watchdog.ps1
# Requires: The ./src/tailwind-input.css file is required to build the tailwind output.css

npx tailwindcss -i ./src/tailwind-input.css -o ./src/static/output.css --watch