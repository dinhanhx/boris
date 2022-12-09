1. Get the remoteAddress of the remote machines, both slave and master. Example: ubuntu@ec2-13-212-195-65.ap-southeast-1.compute.amazonaws.com
2. Copy files `10-kubeadm.conf` to both machines. Copy file `master.sh` to master machine and `slave.sh` to slave machine.
```
scp -i keyfile origin_file_location final_destination
```
Example:
```
scp -i ~/.ssh/keypair.pem ubuntu@ec2-13-212-195-65.ap-southeast-1.compute.amazonaws.com:/home/ubuntu/file_to_copy.txt ~/Local_destination/

```
3. Run the `master.sh` file on the master node in `sudo bash` and then copy the generated file `/home/ubuntu/join.sh` to local machine.
4. Copy the `join.sh` file to the slave machine, then run the bash file `slave.sh` in `sudo bash`
