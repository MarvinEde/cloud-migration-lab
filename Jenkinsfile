pipeline {
    agent any

    stages {
        stage('nettoyage et preparation'){
            steps {
                echo 'Nettoyage de l environnement'
                deleteDir()
                checkout scm
            }
        }
        stage('Audit de securite') {
            steps {
                echo 'Lancement du scanner Python'
                sh 'python3 scripts/scanner.py'
            }
        }
    }
    post {
        success {
            echo 'L audit est valide ! Code sain.'
        }
        failure {
            echo 'ALERTE : Le scanner a detecte des vulnerabilites !'
        }
    }

}