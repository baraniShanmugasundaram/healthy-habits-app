pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    bat 'echo Building the application...'
                    bat 'docker build -t healthy-habits-app:latest .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'echo Running tests...'
                    bat 'echo PYTHONPATH=%PYTHONPATH%'
                    bat 'dir %WORKSPACE%'
                    bat 'dir %WORKSPACE%\\app'
                    bat 'type %WORKSPACE%\\app\\__init__.py'
                    bat 'docker run -it --rm -v %cd%:/app -w /app healthy-habits-app sh -c "export PYTHONPATH=/app && pytest tests/"'
                }
            }
        }

        stage('Code Quality Analysis') {
            steps {
                script {
                    bat 'echo Running code quality analysis...'
                    bat 'sonar-scanner'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'echo Deploying to test environment...'
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Release') {
            steps {
                script {
                    bat 'echo Releasing to production...'
                    bat 'aws deploy create-deployment --application-name healthy-habits-app --deployment-group-name production --s3-location bucket=myBucket,key=myKey,bundleType=zip'
                }
            }
        }

        stage('Monitoring and Alerting') {
            steps {
                script {
                    bat 'echo Setting up monitoring and alerting...'
                    bat 'datadog-agent status'
                }
            }
        }
    }
}
