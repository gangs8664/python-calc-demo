pipeline {
    agent any
    environment {
        PATH = "${env.PATH}:/var/lib/jenkins/.local/bin"
    }
    stages {
        stage('Install') {
            steps {
                sh 'pip install --user -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest -q --tb=short'
            }
        }
    }
}

