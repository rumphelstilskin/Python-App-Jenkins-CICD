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
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'rumphelstilskin', passwordVariable: 'JwiSW7HkBwytPbK')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker tag flask-app rumphelstilskin/flask-app:latest'
                    sh 'docker push rumphelstilskin/flask-app:latest'
                }
            }
        }
        stage('Deploy Docker image to server') {
            steps {
                sshagent(['rumphel']) {
                    sh 'ssh root@212.68.34.217 "docker stop flask-app || true"'
                    sh 'ssh root@212.68.34.217 "docker rm flask-app || true"'
                    sh 'ssh root@212.68.34.217 "docker run -d --name flask-app -p 5000:5000 <dockerhub-username>/<repository-name>:latest"'
                }
            }
        }
    }
}
