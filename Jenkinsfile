pipeline {
  agent any

  // 跳过 Declarative Pipeline 自动 checkout
  options { skipDefaultCheckout() }

  environment {
    BACKEND_IMAGE = 'ai-backend:latest'
  }

  stages {
    stage('Checkout') {
      steps {
        // 用你在凭据里配置的 SSH Key
        git(
          url:      'git@github.com:2022113560/Intelligent-Customer-Service.git',
          branch:   'main',
          credentialsId: 'github-ssh-key'  // 确保这是你在 Jenkins 凭据里新建的 GitHub SSH Key
        )
      }
    }

    stage('Build Backend Docker') {
      steps {
        dir('backend') {
          script {
            docker.build("${env.BACKEND_IMAGE}", '.')
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
        // 确保 docker-compose.yml 在仓库根目录
        sh 'docker-compose up -d --build'
      }
    }
  }

  post {
    always   { echo '流水线执行结束' }
    success  { echo '构建成功！' }
    failure  { echo '构建失败，请检查日志' }
  }
}
