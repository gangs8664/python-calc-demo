pipeline {
    agent any
    environment {
        PATH = "${env.PATH}:/var/lib/jenkins/.local/bin"
    }
    stages {
        stage('Install') {
            steps {
                sh 'pip install --user -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest -q --tb=short'
            }
        }
	stage('SonarQube Analysis') {
            steps {
                // 'My SonarQube'는 젠킨스 '시스템 설정'에서 지정한 SonarQube 서버의 'Name'
                withSonarQubeEnv('My SonarQube') {
                    // SonarQube Scanner 실행 (파이썬 프로젝트용)
                    // 'Default SonarScanner'는 젠킨스 '글로벌 도구 설정'에서 지정한 스캐너의 'Name'
                    sh """
                    . venv/bin/activate && \\ # 파이썬 가상 환경 활성화
                    ${tool 'Default SonarScanner'}/bin/sonar-scanner \\
                      -Dsonar.projectKey=my-python-calculator \\ # SonarQube에 표시될 고유 키 (원하는 이름으로 변경)
                      -Dsonar.projectName='Python Calculator' \\ # SonarQube에 표시될 프로젝트 이름
                      -Dsonar.sources=. \\ # 분석할 소스 코드 경로 (현재 디렉토리)
                      -Dsonar.language=py # 분석 언어 지정
                    """
                }
            }
        }
    }
}

