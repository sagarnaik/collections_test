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
                    files = gapi.get_test_files()
                    wch = gapi.while_check()
                    cnt = gapi.if_check()
                    println files
                    println wch
                    println cnt
                    
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
