pipeline {
    agent any

    parameters {
        choice(name: 'DEPLOYMENT_ACTION', choices: ['DEPLOY', 'ROLLBACK'])
        choice(name: 'ENVIRONMENT', choices: ['UAT', 'PRODUCTION'])
        string(name: 'VERSION', defaultValue: '4.2.1')
        choice(name: 'CONFIRM_PROD', choices: ['NO', 'YES'])
    }

    environment {
        IMAGE = 'retail-app'
        CONTAINER = 'retail-app'
        PORT = '8081'
    }

    stages {

        stage('Validate') {
            steps {
                script {
                    echo "Git commit: ${env.GIT_COMMIT}"

                    if (params.ENVIRONMENT == 'PRODUCTION' &&
                        params.CONFIRM_PROD != 'YES') {
                        error('Production confirmation required')
                    }

                    bat "git tag --list v${params.VERSION}"
                }
            }
        }

        stage('Build') {
            when {
                expression { params.DEPLOYMENT_ACTION == 'DEPLOY' }
            }
            steps {
                bat "docker build -t ${IMAGE}:${params.VERSION} ."
            }
        }

        stage('Deploy & Health Check') {
            when {
                expression { params.DEPLOYMENT_ACTION == 'DEPLOY' }
            }
            steps {
                script {
                    try {
                        bat """
                        docker run -d --name ${CONTAINER}-new ^
                          -p ${PORT}:${PORT} ^
                          ${IMAGE}:${params.VERSION}
                        """

                        bat 'powershell -Command "Start-Sleep 15"'

                        bat """
                        powershell -Command "if ((docker inspect -f '{{.State.Health.Status}}' ${CONTAINER}-new) -ne 'healthy') { exit 1 }"
                        """

                        echo "New version ${params.VERSION} is healthy"
                    }
                    catch (e) {
                        echo "Health check failed - rolling back"
                        bat "docker rm -f ${CONTAINER}-new 2>NUL || exit /b 0"
                        error("Deployment failed - rollback required")
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful"
        }
    }
}