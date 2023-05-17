pipeline {
    agent any
    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Push Docker image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker tag flask-app rumphelstilskin/flask-app:latest'
                    sh 'docker push rumphelstilskin/flask-app:latest'
                }
            }
        }
        stage('Deploy Docker image to server') {
            steps {
                sshagent(credentials: ['ssh-credentials']) {
                    sh 'ssh root@195.155.131.103 "docker rm -f flask-app || true"'
                    sh 'ssh root@195.155.131.103 "docker pull rumphelstilskin/flask-app:latest || true"'
                    sh 'ssh root@195.155.131.103 "docker run -d --name flask-app -p 5000:5000 rumphelstilskin/flask-app:latest"'
                }
            }
        }
    }
}
