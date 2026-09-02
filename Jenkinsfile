pipeline {

    agent any

    environment {
        IMAGE_NAME = "devops-security-testing"
        IMAGE_TAG = "v1"
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

        stage('Unit Testing - PyTest') {
            steps {
                sh '''
                    pytest test_app.py
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
                    docker build \
                    -t ${IMAGE_NAME}:${IMAGE_TAG} .
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

        stage('Run Application') {
            steps {
                sh '''
                    docker rm -f devops-app || true

                    docker run -d \
                    --name devops-app \
                    -p 5000:5000 \
                    ${IMAGE_NAME}:${IMAGE_TAG}

                    sleep 10
                '''
            }
        }

        stage('API Testing - Newman') {
            steps {
                sh '''
                    newman run postman/api-tests.json
                '''
            }
        }

        stage('OWASP ZAP Scan') {
            steps {
                sh '''
                    docker run --rm \
                    --network host \
                    zaproxy/zap-stable \
                    zap-baseline.py \
                    -t http://localhost:5000 \
                    -r zap-report.html
                '''
            }
        }

        stage('UI Testing - Selenium') {
            steps {
                sh '''
                    pytest selenium/test_ui.py
                '''
            }
        }
    }

    post {

        always {
            sh '''
                docker rm -f devops-app || true
            '''
        }
    }
}
