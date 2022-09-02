# creating (based on a local machine, using Minikube)
docker build -t ldapapp . <br />
minikube image load ldapapp <br />
kubectl create secret generic openldap --from-literal=adminpassword=adminpassword --from-literal=users=user01,user02 --from-literal=passwords=password01,password02 <br />
kubectl apply -f .<br />
# please wait for a few seconds for the pods to start
kubectl port-forward <ldpa-pod-name> 5000:<any-port-wished>

# cleaning
kubectl delete deployments.apps --all <br />
kubectl delete secrets --all <br />
kubectl delete service --all <br />

# if port forwarding still remains
ps -ef|grep port-forward <br />
kill -9 <process number>