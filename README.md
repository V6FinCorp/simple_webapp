# Simple Webapp

A minimal Flask web application for testing and deploying to Azure Web Apps.

Quickstart (Azure App Service - Python)

1. Create a resource group and app service plan (replace names):

   az group create --name myResourceGroup --location "West US"
   az appservice plan create --name myPlan --resource-group myResourceGroup --sku B1 --is-linux

2. Create the web app and deploy (using local git or ZIP deploy):

   az webapp create --resource-group myResourceGroup --plan myPlan --name <your-app-name> --runtime "PYTHON|3.11"
   az webapp deployment source config-zip --resource-group myResourceGroup --name <your-app-name> --src simple_webapp.zip

3. Alternatively, deploy as a container using the provided Dockerfile.

Local run:

   python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py

