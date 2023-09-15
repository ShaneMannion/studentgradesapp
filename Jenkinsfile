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
                sh 'ls -lrt'
                sh 'cd Python'
                sh 'pwd'
                sh 'ls -lrt'
                sh 'pip3 -V'    
                sh "pwd"
                dir('Python') {
                    sh "pwd"
                    sh 'ls -lrt'
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest'
                }
                sh "pwd"
                sh 'python3 --version'

            }
        }
        stage('Unit Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Code review') {
            steps {
                sh 'pylint'
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
