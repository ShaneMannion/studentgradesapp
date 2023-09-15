pipeline {
    agent { 
        node {
            label 'Python-Node'
        }
    }
    stages {
        stage('Unit Test') {
            steps {
                sh 'cd ./Python && pytest'
            }
        }
        stage('Code review') {
            steps {
                sh 'cd ./Python && pylint'
            }
        }  
    }
    post {
        success {
            echo 'Job completed successfully'
        }
        failure {
            echo 'Job failed'
        }
    }
}
