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
                }
                sh "pwd"
                sh 'python3 -version'
                sh 'pip3 install requirements.txt'
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
