node {
  stage ("Checkout") {
        checkout scm
    }
    
 
  stage ('Docker build') {
  docker.build('agrostardemoapp')
  }
  stage ('Docker Push'){
  docker.withRegistry('https://081499153638.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:AWS_CREDS') {
    docker.image('agrostardemoapp').push('latest')
  }
  }
  stage ('kubectl test'){
    withKubeConfig([credentialsId: 'kubernetes-jenkins-deployer', serverUrl: 'https://19F8661A74AE5A4F0C79BD627A0FA346.gr7.us-east-1.eks.amazonaws.com']){
    
      sh 'kubectl apply -f deployment.yml'   
    }
  }
  
}
