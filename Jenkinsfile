node {
  stage ("Checkout") {
        checkout scm
    }
    
 
  stage 'Docker build'
  docker.build('agrostardemoapp')
 
  stage 'Docker push'
  docker.withRegistry('081499153638.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:agrostardemoapp-ecr-credentials') {
    docker.image('agrostardemoapp').push('latest')
  }
}
