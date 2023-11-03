pipeline {
    agent { 
        node {
            label 'Python-Node'
        }
    }
    stages {
        stage('setup') {
            steps {
                sh 'pwd'
                dir('Python') {
                    sh "pwd"
                    sh 'ls -lrt'
                    sh "python3 -m venv grades-app-env"
                    sh "source grades-app-env/bin/activate"
                    sh 'pip3 install -r requirements.txt'
                    sh 'pylint *.py'
                }
            }
        }
        stage('Unit Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Teardown') {
            steps {
                sh "rm -r venv/"
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
