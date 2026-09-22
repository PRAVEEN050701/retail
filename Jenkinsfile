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
        OLD_VERSION = '4.2.1'
    }

    stages {

        stage('Validate') {
            steps {
                script {
                    echo "Commit: ${env.GIT_COMMIT}"

                    if (params.ENVIRONMENT == 'PRODUCTION' &&
                        params.CONFIRM_PROD != 'YES') {
                        error('Production confirmation required')
                    }

                   bat "\"C:\\Program Files\\Git\\cmd\\git.exe\" tag --list v${params.VERSION}"
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

        stage('Deploy') {
            when {
                expression { params.DEPLOYMENT_ACTION == 'DEPLOY' }
            }
            steps {
                script {
                    try {
                        echo "OLD VERSION: ${OLD_VERSION}"
                        echo "NEW VERSION: ${params.VERSION}"

                        bat """
                        docker rm -f retail-new 2>NUL || exit /b 0
                        docker run -d --name retail-new ^
                          -p 8081:8081 ^
                          ${IMAGE}:${params.VERSION}
                        """

                        bat 'powershell -Command "Start-Sleep -Seconds 15"'

                        bat """
                        powershell -Command "if ((docker inspect -f '{{.State.Health.Status}}' retail-new) -ne 'healthy') { exit 1 }"
                        """

                        echo "NEW VERSION HEALTHY"
                    }
                    catch (e) {
                        echo "HEALTH CHECK FAILED"
                        echo "ROLLING BACK TO ${OLD_VERSION}"

                        bat "docker rm -f retail-new 2>NUL || exit /b 0"

                        bat """
                        docker run -d --name retail-app ^
                          -p 8081:8081 ^
                          ${IMAGE}:${OLD_VERSION}
                        """

                        bat 'powershell -Command "Start-Sleep -Seconds 15"'

                        bat """
                        powershell -Command "if ((docker inspect -f '{{.State.Health.Status}}' retail-app) -ne 'healthy') { exit 1 }"
                        """

                        echo "ROLLBACK VERIFIED: ${OLD_VERSION}"

                        error('Deployment failed; rollback completed')
                    }
                }
            }
        }
    }

    post {
        success {
            echo "DEPLOYMENT SUCCESSFUL"
        }
        failure {
            echo "DEPLOYMENT FAILED - CHECK ROLLBACK"
        }
    }
}