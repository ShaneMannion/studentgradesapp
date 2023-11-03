pipeline {
    agent { 
        node {
            label 'Python-Node'
        }
    }
    stages {
        stage('setup') {
            steps {
                dir('Python') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest'
                    sh 'pylint *.py'
                    sh 'ls -lrt'
                }
            }
        }
    }
}
