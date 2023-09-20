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
                    //sh 'pylint --rcfile=pylint.cfg funniest/ $(find . -maxdepth 1 -name "*.py" -print) --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint.log || echo "pylint exited with $?"'
                    sh 'pylint *.py > pylint_out.txt'
                    sh "sed 'x;$!d' pylint_out.txt"
                    sh "rm -r venv/"
                    echo "linting Success, Generating Report"

                    warnings canComputeNew: false, canResolveRelativePaths: false, defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', parserConfigurations: [[parserName: 'PyLint', pattern: '*']], unHealthy: ''
                }
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
