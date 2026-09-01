pipeline {

    agent any

    environment {
        IMAGE_NAME = "myapp"
        IMAGE_TAG  = "v1"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: '<YOUR_GITHUB_REPO_URL>'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                sh '''
                    pytest
                '''
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh '''
                    trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 1 \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Docker Image Check') {
            steps {
                sh '''
                    docker images
                '''
            }
        }
    }
}
