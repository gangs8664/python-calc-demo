pipeline {
    agent any

    environment {
        PATH = "${env.PATH}:/var/lib/jenkins/.local/bin" // 기존 PATH 설정 유지
    }

    stages {
        stage('Install Dependencies & Setup Venv') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest -q --tb=short'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                // 'My SonarQube'는 젠킨스 '시스템 설정'에서 지정한 SonarQube 서버의 'Name'
                withSonarQubeEnv('My SonarQube') {
                    // [수정된 부분: 'script' 블록 추가 및 sonarScannerPath 변수 사용]
                    script { // 'script' 블록을 사용하여 복잡한 Groovy 로직을 실행합니다.
                        // 'tool' 함수를 사용하여 SonarScanner의 실제 경로를 미리 계산하여 변수에 저장합니다.
                        // 'Default SonarScanner'는 젠킨스 '글로벌 도구 설정'에서 지정한 스캐너의 'Name'입니다.
                        def sonarScannerPath = tool 'Default SonarScanner'

                        // 이제 'sh' 명령은 백슬래시 없이 한 줄로, 깔끔하게 실행됩니다.
                        // ${sonarScannerPath}는 미리 계산된 실제 경로로 치환됩니다.
                        sh ". venv/bin/activate && ${sonarScannerPath}/bin/sonar-scanner -Dsonar.projectKey=my-calculator-simple -Dsonar.projectName='Simple Python Calculator' -Dsonar.sources=. -Dsonar.language=py -Dsonar.sourceEncoding=UTF-8 -Dsonar.exclusions=venv/**"
                    }
                }
            }
        }
    }
}
