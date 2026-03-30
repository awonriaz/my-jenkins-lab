pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/awonriaz/my-jenkins-lab.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Simulating a build..." && sleep 5'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Simulating tests..." && sleep 3'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Simulating deployment..."' // Placeholder for actual deployment command
            }
        }
    }
}
