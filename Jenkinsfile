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
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'rumphelstilskin', passwordVariable: 'dckr_pat_Ep1Mll-D0nj_s3WioNaorHrLgX0')]) {
                    sh 'docker login -u $rumphelstilskin -p $dckr_pat_Ep1Mll-D0nj_s3WioNaorHrLgX0'
                    sh 'docker tag flask-app rumphelstilskin/flask-app:latest'
                    sh 'docker push flask-app rumphelstilskin/flask-app:latest'
                }
            }
        }
        stage('Deploy Docker image to server') {
            steps {
                sshagent(['<ssh-credentials>']) {
                    sh 'ssh <user>@<server> "docker stop flask-app || true"'
                    sh 'ssh <user>@<server> "docker rm flask-app || true"'
                    sh 'ssh <user>@<server> "docker run -d --name flask-app -p 5000:5000 <dockerhub-username>/<repository-name>:latest"'
                }
            }
        }
    }
}
