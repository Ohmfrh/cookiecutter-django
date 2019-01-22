String cron_string = BRANCH_NAME == "master" ? "H 2 * * *" : "*/20 * * * *"

pipeline {
    agent any

    triggers {
        pollSCM(cron_string)
    }

    stages {

        stage('Build test Docker images') {
            steps {
                sh "docker-compose -f test.yml build"
            }
        }

        stage('Test project') {
            steps {
                sh "docker-compose -f test.yml up --force-recreate --abort-on-container-exit"
                sh "docker-compose -f test.yml down -v"
            }
        }

        stage('Deploy') {
            when {
              expression {
                env.BRANCH_NAME == 'master'
              }
            }
            steps {
                sh "(cd deployment; ./deploy.sh)"
            }
        }
    }
    post {
        always {
            echo 'Sending email'

            emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                recipientProviders: [
                            [$class: 'CulpritsRecipientProvider'],
                            [$class: 'DevelopersRecipientProvider'],
                            [$class: 'RequesterRecipientProvider']
                        ],
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"

        }
    }
}
