pipeline {
    agent any

    environment {
        // Docker 镜像名称，可根据需要修改
        BACKEND_IMAGE = 'ai-backend:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Backend Docker') {
            steps {
                dir('backend') {
                    script {
                        // 构建后端镜像并打标签
                        docker.build(BACKEND_IMAGE, '.')
                    }
                }
            }
        }
        stage('Run Backend Tests') {
            steps {
                dir('backend') {
                    sh 'pytest --maxfail=1 --disable-warnings -q'
                }
            }
        }
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }
        stage('Docker Compose Up') {
            steps {
                // 在根目录执行 docker-compose，确保 docker-compose.yml 在根目录
                sh 'docker-compose up -d --build'
            }
        }
    }
    post {
        always {
            echo '流水线执行结束'
        }
        success {
            echo '构建成功！'
        }
        failure {
            echo '构建失败，请检查日志'
        }
    }
}
