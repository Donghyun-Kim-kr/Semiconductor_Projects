# FDC/SPC 처리 데이터 설정
## 목적
실시간 센서 데이터 및 SPC 기반 반도체 공정 조치 알고리즘 구현을 위한 데이터 세팅

## 기능
csv 형태로 데이터 로드 기능 추가
알고리즘 테스트, 공정적 대처 시뮬레이션을 위한 더미 데이터 생성 기능 추가

## 데이터 및 영향 예측
### 대상
Plasma 활용 Etch 공정의 센서 데이터 모사

- Run_ID : 정수 형태 웨이퍼 가공 단위 식별자 역할
- Timestamp : 챔버에서 센서 데이터 측정된 시간
- Step_No : 정수 형태 (1~5) / 공정 중 진행되는 단계, Step 고려한 변수 값 범위 설정
- Pressure : 148.0 ~ 152.0 mTorr 압력 - 쓰로틀 밸브 오작동 시 조치 필요
  - 과주입 : 과도한 식각
  - 과부족 : 식각 정도 미비
- RF_Power : 595.0~605.0 W RF Power - 플라즈마 생성 정도 조절, 605W 초과 시 과도 식각
- Gas_Flow_Ar : 98,0 ~ 102.0 sccm - 물리적 식각 관련, 부족하면 스퍼터링 감소
- Gas_Flow_CF4 : 49.0~51.0 sccm - 화학적 식각 관련, 과주입시 프로파일 이슈
- Temp_He_Focus : 78.5~81.5 C - He Focus Ring 후면 냉각 온도
- Defect_Label : 0 정상 / 1 불량 - EDC 전기적 테스트 결과 최종 양부 판정

### Step 단위 데이터 슬라이싱
<img width="536" height="218" alt="image" src="https://github.com/user-attachments/assets/b312dbb5-a358-4482-99cb-3b482f1de50b" />

각 스텝별 평균 압력/RF Power / Temp 등을 분리해서 적용

### 결측치
<img width="372" height="217" alt="image" src="https://github.com/user-attachments/assets/dcb447f9-b79c-4b18-9599-abfa4b608203" />

현재 결측치는 정의되지 않은 상태
