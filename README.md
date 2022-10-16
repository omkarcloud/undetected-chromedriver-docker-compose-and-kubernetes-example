To Run Docker Compose Example

```
git clone https://github.com/Chetan11-Dev/undetected-chromedriver-docker-compose-and-kubernetes-example
cd docker-compose-example
docker-compose  build
docker-compose  up
```

To Run Kubernetes Example

```
git clone https://github.com/Chetan11-Dev/undetected-chromedriver-docker-compose-and-kubernetes-example
cd kubernetes-example
kubectl apply -f undetected-chromedriver-job
kubectl get pods
kubectl get pods
kubectl logs -f undetected-chromedriver-job-cb554c8bc-qs2ll
```
