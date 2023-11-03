pipeline {
    agent { 
        node {
            label 'Python-Node'
        }
    }
    stages {
        stage('Lint') {
            steps {               
                dir('Python') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pylint *.py --exit-zero'
                }

            }
        }
        stage('Test') {
            steps {
                dir('Python') {
                    sh 'pytest'
                }
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
