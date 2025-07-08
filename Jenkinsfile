pipeline {
    agent any // 빌드를 실행할 젠킨스 에이전트

    environment {
        PATH = "${env.PATH}:/var/lib/jenkins/.local/bin" // 기존 PATH 설정 유지 (필요시)
    }

    stages {
        // [수정된 부분: stage 이름 변경 및 venv 생성 추가]
        stage('Install Dependencies & Setup Venv') {
            steps {
                // 파이썬 가상 환경 생성 (이 명령어가 venv 폴더를 만듭니다!)
                sh 'python3 -m venv venv'
                // 필요한 파이썬 패키지 설치 (이제 venv 안에 설치됩니다)
                sh '. venv/bin/activate && pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Run Tests') { // stage 이름 변경 (Test에서 Run Tests로)
            steps {
                // 파이썬 테스트 실행
                sh '. venv/bin/activate && pytest -q --tb=short'
            }
        }
        // --- 여기부터 SonarQube 분석 단계 추가 ---
        stage('SonarQube Analysis') {
            steps {
                // 'My SonarQube'는 젠킨스 '시스템 설정'에서 지정한 SonarQube 서버의 'Name'
                withSonarQubeEnv('My SonarQube') {
                    // SonarQube Scanner 실행 (파이썬 프로젝트용)
                    // 'Default SonarScanner'는 젠킨스 '글로벌 도구 설정'에서 지정한 스캐너의 'Name'
                    sh """
                    . venv/bin/activate && \\ # 파이썬 가상 환경 활성화 (여기서 venv/bin/activate를 찾을 것입니다)
                    ${tool 'Default SonarScanner'}/bin/sonar-scanner \\
                      -Dsonar.projectKey=my-python-calculator \\ # **여기를 수정하세요: 소나큐브에 표시될 고유 키 (예: 영문 소문자, 숫자, 하이픈만 사용)**
                      -Dsonar.projectName='Python Calculator' \\ # **여기를 수정하세요: 소나큐브에 표시될 프로젝트 이름 (원하는 이름으로 변경)**
                      -Dsonar.sources=. \\ # 분석할 소스 코드 경로 (현재 디렉토리)
                      -Dsonar.language=py \\ # 분석 언어 지정
                      -Dsonar.sourceEncoding=UTF-8 \\ # 소스 코드 인코딩 - 특별한 경우 아니면 그대로 두세요
                      -Dsonar.python.version=3.9 # **여기를 수정하세요: 실제 사용하는 파이썬 버전에 맞게 (예: 3.8, 3.10, 3.11 등)**
                    """
                }
            }
        }
        // --- Quality Gate Check 단계는 일단 생략합니다. ---
    }
}
