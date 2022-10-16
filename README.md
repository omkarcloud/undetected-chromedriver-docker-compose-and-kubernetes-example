Welcome my dear Rat,
Here is an example to demonstrate a Kubernetes and docker-compose example.

To Run Docker Compose Example run the following commands

```
git clone https://github.com/Chetan11-Dev/undetected-chromedriver-docker-compose-and-kubernetes-example
cd docker-compose-example
docker-compose  build
docker-compose  up
```

Output:
![alt text](https://github.com/Chetan11-Dev/undetected-chromedriver-docker-compose-and-kubernetes-example/blob/master/images/dc.png?raw=true)

To Run Kubernetes Example run the following commands

```
git clone https://github.com/Chetan11-Dev/undetected-chromedriver-docker-compose-and-kubernetes-example
cd kubernetes-example
kubectl apply -f undetected-chromedriver-job.yaml
kubectl get pods
kubectl get pods
kubectl logs -f undetected-chromedriver-job-n7kdr
```

Output:
![alt text](https://github.com/Chetan11-Dev/undetected-chromedriver-docker-compose-and-kubernetes-example/blob/master/images/kube.png?raw=true)
