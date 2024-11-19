pipeline {
    agent any  // This will run the pipeline on any available agent
    
    environment {
        // Define environment variables for the app
        APP_DIR = '/path/to/your/app'  // Path to the app directory on the agent
        BRANCH = 'main'                // Branch to deploy
        BUILD_DIR = 'build'            // Build output directory
        REMOTE_SERVER = 'user@server.com'  // Remote server SSH login
        DEPLOY_DIR = '/var/www/app'    // Remote server deploy directory
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                script {
                    echo "Checking out branch: ${BRANCH}"
                    git branch: "${BRANCH}", url: 'https://github.com/your/repository.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Node.js dependencies
                script {
                    echo "Installing dependencies..."
                    sh 'npm install'
                }
            }
        }

        stage('Build') {
            steps {
                // Run the build command (e.g., 'npm run build')
                script {
                    echo "Running build..."
                    sh 'npm run build'    sh 'myscript.sh'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the build to the remote server using rsync or SCP
                script {
                    echo "Deploying build to the server..."
                    sh """
                    rsync -avz --delete ${BUILD_DIR}/ ${REMOTE_SERVER}:${DEPLOY_DIR}/
                    """
                }
            }
        }

        stage('Restart Server') {
            steps {
                // Optionally, restart the server to apply changes (this depends on your app setup)
                script {
                    echo "Restarting server..."
                    sh """
                    ssh ${REMOTE_SERVER} 'sudo systemctl restart myapp-service'
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed!"
        }
    }
}
