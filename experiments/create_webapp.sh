kubectl create deployment my-flask-app --image=poroko/flask-demo-app
kubectl expose deployment my-flask-app --port=8080 --target-port=5000 --type=NodePort
kubectl get service my-flask-app