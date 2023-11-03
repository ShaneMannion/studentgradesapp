pipeline {
    agent { 
        node {
            label 'Python-Node'
        }
    }
    stages {
        stage('Lint') {
            steps {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pylint ./Python'
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
}
