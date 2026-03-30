pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/awonriaz/my-jenkins-lab.git'
            }
        }
        stage('Train ML Model') {
            steps {
                sh 'python3 train_model.py'
            }
        }
        stage('Build Application') {
            steps {
                sh 'make build'
            }
        }
        stage('Test Application') {
            steps {
                sh 'make test'
            }
        }
        stage('Predict Build Outcome') {
            steps {
                sh 'python3 predict_build_outcome.py'
            }
        }
        stage('Deploy Application') {
            steps {
                sh 'make deploy'
            }
        }
    }
}
