# File: fastapi-serve-forever.ps1
# Requires: The fastAPI/app.py file with wa inside as FastAPI class.

uvicorn.exe fastAPI.app:wa --reload