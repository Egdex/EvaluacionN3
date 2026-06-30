pipeline {
    agent any

    stages {

        stage('Construcción') {
            steps {
                echo 'Construyendo la imagen Docker...'
                sh 'docker build -t flask-app-segura .'
            }
        }

        stage('Despliegue') {
            steps {
                sh 'docker rm -f app-prod || true'
                sh 'docker run -d -p 5001:5000 --name app-prod flask-app-segura'
            }
        }

        stage('Prueba de Seguridad') {
            steps {
                sh 'docker run --rm --network host softwaresecuritydotorg/zap-stable zap-baseline.py -t http://localhost:5001 || true'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente.'
        }
        failure {
            echo 'El pipeline presentó errores.'
        }
    }
}