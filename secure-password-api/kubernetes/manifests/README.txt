kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml

FastAPI app serves the Swagger UI under /docs