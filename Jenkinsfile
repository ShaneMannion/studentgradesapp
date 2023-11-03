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
                    sh 'pytest'
                    sh 'pylint *.py'
                    sh "deactivate"
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
