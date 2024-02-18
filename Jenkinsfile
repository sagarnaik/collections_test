uname = UserName
testname = TestName
def (a, b, c) = [20, 30, 40]
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script {
                    if (testname == 'Calculator'){
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
                    if (testname == 'Calculator'){
                        println testname
                        sh 'python3 test_calc.py'
                    } else {
                        println testname
                        sh 'pytest test_k8s.py'
                    }
                        
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
