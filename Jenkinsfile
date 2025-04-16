pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/Abhinav-ep/Jenkins_Test1.git'
    }

    stages {
        stage('Init') {
            steps {
                echo '✅ Stage 1 - Init complete.'
            }
        }

        stage('Setup') {
            steps {
                echo '✅ Stage 2 - Setup complete.'
            }
        }

        stage('Compare With Template') {
            steps {
                echo 'Comparing script with template...'

                script {
                    def result = sh(script: 'python3 validate_template.py', returnStatus: true)

                    if (result != 0) {
                        echo '❌ Template mismatch. Reverting last commit...'

                        withCredentials([usernamePassword(
                            credentialsId: 'github-creds',
                            usernameVariable: 'GIT_USER',
                            passwordVariable: 'GIT_PASS'
                        )]) {
                            sh '''
                                git config user.email "abhinavsureshep2@gmail.com"
                                git config user.name "Abhinav-ep"
                                git remote set-url origin https://${GIT_USER}:${GIT_PASS}@github.com/Abhinav-ep/Jenkins_Test1.git
                                git reset --hard HEAD~1
                                git push origin HEAD:refs/heads/main --force
                            '''
                        }

                        error("Script does not match the template.")
                    }
                    else {
                        sh 'script3.sh'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying project...'
            }
        }
    }
}
