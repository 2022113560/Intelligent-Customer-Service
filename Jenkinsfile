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

    stage('Init SSH') {
      steps {
        // 确保 ~/.ssh 存在并添加 GitHub 主机密钥
        sh '''
          mkdir -p ~/.ssh
          chmod 700 ~/.ssh
          ssh-keyscan github.com >> ~/.ssh/known_hosts
        '''
      }
    }

    stage('Checkout') {
      steps {
        // 用 ssh-agent 插件加载你的私钥凭据
        sshagent(['gitlab-ssh-key']) {
          // 这里使用 declarative git 步骤也可以，但用 shell clone 最灵活
          sh 'git clone git@github.com:2022113560/Intelligent-Customer-Service.git .'
        }
      }
    }

    stage('Build Backend Docker') {
      steps {
        dir('backend') {
          script { docker.build(BACKEND_IMAGE, '.') }
        }
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
