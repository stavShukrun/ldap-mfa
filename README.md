# Ldap and MFA
A simple flask app that allow you to conact with LDAP (Lightweight Directory Access Protocol) and MFA (Multi Factor Authentication).
The app can run localy with docker compose or with kubernetes(I use minikube).

## Work tree
```
.
├── Dockerfile
├── README.md
├── app
│   ├── app.py
│   ├── form.py
│   ├── ldap_authentication.py
│   ├── requirements.txt
│   ├── settings.py
│   └── templates
│       ├── index.html
│       ├── login.html
│       └── mfa.html
├── docker-compose.yml
└── k8s
    ├── app
    │   └── app-deployment.yaml
    └── openldap
        ├── ldap-deployment.yaml
        └── ldap-service.yaml
```

## Run localy
Run the comnd:
```
docker-compose up -d --build
```
Then you can enter http://localhost:5000 , Username and Password ar in ___ file.

## Set minikube
go to - https://minikube.sigs.k8s.io/docs/start/

## Run with k8s (Minikube)

```
docker build -t app .
cd k8s
minikube image load app 
cd openldap
kubectl create secret generic openldap --from-literal=adminpassword=adminpassword --from-literal=users=user01,user02 --from-literal=passwords=password01,password02
kubectl apply -f .
cd ..
cd app
kubectl apply -f .
```
Wait until pods are up (few seconds)
```
kubectl port-forward <app-pod-name> 5000:<any-port-wished>
```

## cleaning
```
kubectl delete deployments.apps --all
kubectl delete secrets --all
kubectl delete service --all
```
If port forward prosess is still up :
```
ps -ef | grep port-forward
kill -9 <process number>
```

stop minikube :
```
minikube stop
```