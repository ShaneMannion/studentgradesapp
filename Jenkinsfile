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
                    sh 'pylint *.py'
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
}
