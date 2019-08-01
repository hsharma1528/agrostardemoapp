# demoapp
Flask based demo app.

## Prerequisite
 - Python3
 - pip3

## How to install
- Clone project 
- execute "pip install -r requirement.txt"

## How to run project 
- "python demoapp.py"

## How to confirm running app
- open your browser with below URL <br />
    - http://127.0.0.1/           <br /># It will display output as "Welcome to Demo app" <br />
    - http://127.0.0.1/hostname   <br /># It will display hostname of system <br />
    - http://127.0.0.1/status     <br /># It will display status of app <br />

- Can also use curl command for testsing<br />
  'curl http://127.0.0.1'

    you will get the host name of the system 
       
 ## Containerisation
    Dockerfile is used the build the image which exposes port 80
 
 ## K8s deployment
    deployment.yml creates a deployment and exposes the service as type load balancer, when deployed on a K8s cluster on AWS it creates a LB
## Jenkinsfile
   Jenkinsfile is used for pipeline as a code in Jenkins. It checksout the code, build the image, push it to ECR and deploys to EKS cluster with help of kubernetes-cli plugin. A service account was created and added to Jenkins Credentials
   
## EKS setup on AWS
   # Install eksctl using below commands
       curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
       sudo mv /tmp/eksctl /usr/local/bin
   # Create EKS cluster using eksctl 
     eksctl create cluster --name agstareks --version 1.13 --nodegroup-name standard-workers --node-type t3.medium --nodes 1 --nodes-min 1 --nodes-max 2 --node-ami auto
    
   # Install kubectl 
     
   # Create Service account, clusterrolebinding for SA and get the token
      kubectl create sa jenkins-deployer
      kubectl create clusterrolebinding jenkins-depoyer-role --clusterrole=cluster-admin --serviceaccount=default:jenkins-deployer
      kubectl get secrets
      kubectl describe secret jenkins-deployer-token-ms6kc
   # Add the credentials in Jenkins Credentials Manager
      
      
       
      
   
