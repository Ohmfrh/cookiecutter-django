String cron_string = BRANCH_NAME == "master" ? "H 3 * * *" : "*/20 * * * *"

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
}
