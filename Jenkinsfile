pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'echo "Building the application..."'
                    sh 'docker build -t healthy-habits-app:latest .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'echo "Running tests..."'
                    sh 'pytest tests/'
                }
            }
        }

        stage('Code Quality Analysis') {
            steps {
                script {
                    sh 'echo "Running code quality analysis..."'
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'echo "Deploying to test environment..."'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Release') {
            steps {
                script {
                    sh 'echo "Releasing to production..."'
                    sh 'aws deploy create-deployment --application-name healthy-habits-app --deployment-group-name production --s3-location bucket=myBucket,key=myKey,bundleType=zip'
                }
            }
        }

        stage('Monitoring and Alerting') {
            steps {
                script {
                    sh 'echo "Setting up monitoring and alerting..."'
                    sh 'datadog-agent status'
                }
            }
        }
    }
}
