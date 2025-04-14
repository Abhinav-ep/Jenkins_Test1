pipeline {
    agent any

    triggers {
        pollSCM('*/2 * * * *') 
    }

    environment {
        SCRIPT_PATH = 'scripts/script1.sh'
        TEMPLATE_PATH = 'templates/template1.sh'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Stage 1 - Init') {
            steps {
                echo '✅ Stage 1 - Init complete.'
            }
        }

        stage('Stage 2 - Setup') {
            steps {
                echo '✅ Stage 2 - Setup complete.'
            }
        }

        stage('Compare With Template') {
            steps {
                echo '🔍 Comparing script with template...'
                script {
                    try {
                        sh 'python3 validate_template.py'
                    } catch (Exception e) {
                        echo '❌ Template mismatch. Reverting last commit...'
                        sh '''
                            git config user.email "jenkins@example.com"
                            git config user.name "Jenkins"
                            git reset --hard HEAD~1
                            git push origin HEAD --force
                        '''
                        error("Validation failed — commit reverted.")
                    }
                }
            }
        }

        stage('Stage 3 - Build') {
            steps {
                echo '🚧 Stage 3 - Build in progress...'
            }
        }

        stage('Stage 4 - Deploy') {
            steps {
                echo '🚀 Stage 4 - Deployment in progress...'
            }
        }
    }
}
