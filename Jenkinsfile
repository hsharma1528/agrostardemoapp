node {
  stage ("Checkout") {
        checkout scm
    }
    
 
  stage 'Docker build'
  docker.build('agrostardemoapp')
 
  stage 'Docker push'
  docker.withRegistry('081499153638.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:AWS_CREDS') {
    docker.image('agrostardemoapp').push('latest')
  }
}