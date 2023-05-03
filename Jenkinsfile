pipeline {
    agent any

    stages {
        stage('Build docker image') {
            steps {
                sh 'docker build -t tomerspol/flask-app .'
            }
        }
        stage('Test') {
            steps {
                sh '''
                    docker run -d --name flask-app-test -p 5001:5000 tomerspol/flask-app
                    sleep 6
                    curl localhost:5001
                    docker kill flask-app-test
                '''
            }
        }
      stage('Push image') {
            steps {
                sh '''
                    docker push tomerspol/flask-app
                '''
            }
        }
    }
}
