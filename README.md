# Simple Webapp

Minimal Flask "Hello, world!" app for testing Azure Web App deployment.

Local run:

   python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1; pip install -r requirements.txt; python app.py

Deploy notes: use the provided `Procfile`/`runtime.txt` for Azure App Service (Linux) or the `Dockerfile` to deploy a container.


