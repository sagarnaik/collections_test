def testname = 'Calculator Program Test Cases'
def (a, b, c) = [20, 30, 40]
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
                        println 'Test suite name is ${testname}'
                        println a, b, c
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
