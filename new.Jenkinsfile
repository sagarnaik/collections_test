pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script {
                    sh 'ls'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                script {
                    def ls = sh 'ls'
                    println ls
                    gapi = load "string.groovy"
                    }
                }
            }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
