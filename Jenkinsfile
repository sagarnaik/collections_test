def testname = 'Calculator Program Test Cases'
def a =20
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                script {
                        println testname
                        println a
                        sh 'python3 test_calc.py'
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
