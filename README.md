
- The following app has been development locally and tested for access on **Minikube**. It should work as normal on AKS
- The kubernetes install has a **type:LoadBalancer** as part of deployment. This is for Public access, change the setting accordingly
- FastAPI app serves the Swagger UI under **/docs** (https://hostname:port/docs)

There are two ways to install the app on AKS, below shows the install using manifest files directly

1. Use Visual Studio Code to git pull the repo > Login to AKS remotely > Run the below command from the right location
2. Download the repo locally > Upload the folder to Azure CLI > Login to AKS locally > Run the below commands from the right location

- kubectl apply -f deployment.yaml
- kubectl apply -f service.yaml
- kubectl apply -f hpa.yaml
