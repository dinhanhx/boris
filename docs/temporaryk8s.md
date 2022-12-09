1. Get the `remoteAddress` of the remote machines, both slave and master. Example: ubuntu@ec2-13-212-195-65.ap-southeast-1.compute.amazonaws.com
2. Copy files `10-kubeadm.conf` to both machines.
```
scp -i keyfile origin_file_location final_destination
```
Example:
```
scp -i ~/.ssh/keypair.pem ubuntu@ec2-13-212-195-65.ap-southeast-1.compute.amazonaws.com:/home/ubuntu/file_to_copy.txt ~/Local_destination/

```
3. Run the `master.sh` file on the master node then copy the generated file `/home/ubuntu/join.sh` to local machine.
```
ssh -i <keyfile> <remoteAdress> 'sudo bash -s' < <shell_file.sh>
```
4. Copy the `join.sh` file to the slave machine, then run the bash file `slave.sh` using the above command line. 
5. Deploy the webapp. Only curl at local master machine.
```
kubectl create deployment my-flask-app --image=poroko/flask-demo-app
kubectl expose deployment my-flask-app --port=8080 --target-port=5000 --type=NodePort
kubectl get service my-flask-app
```
