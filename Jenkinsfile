uname = UserName
def testname = 'Calculator Program Test Cases'
def (a, b, c) = [20, 30, 40]
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script {
                    if (testname == 'Calculator Program Test Cases'){
                        echo uname
                        echo "Tested if"
                    } else {
                        echo 'Inside else block'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                script {
                        println testname
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
