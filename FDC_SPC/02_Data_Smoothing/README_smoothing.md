# Data Smoothing
반도체 현장 시계열 센서의 동작과 데이터를 이해, 정제한다.

<br />

## 목적
- Step 3 (실제 식각 반응) 슬라이싱
- 결측치 처리 (삭제x, 경향성 유지하면서 보정)
- Rolling window (이동평균) 기반 데이터 스무딩

<br />

### 데이터 개요
- 평균 150.0mTorr Pressure 데이터
- 노이즈 존재를 가정 (평균 0, 표준편차 3의 정규분포 형태로 설정)
- Drift 상황을 가정 (0~10 구간에서 선형적 증가)
- 결측치 (time stamp 기준 1500~1600 사이)

<br />

## 작업 과정 및 결과

### 레시피 스텝별 슬라이싱
Step_No
1 : 가스 주입
2 : 안정화
3 : 식각 반응
4 : 잔여가스 배기 (1)
5 : 잔여가스 배기 (2)

Step No 3 슬라이싱

<br />

### 결측치 처리
지양할 것
Dropna() -> 결측치 존재하는 timestamp를 통째로 삭제

선택한 방향성
ffill() -> NaN(결측치) 이전 가장 가까운 값으로 채운다 (forward fill)
interpolate(method="linear") -> 선형 보간법으로 결측치 앞과 뒤를 기준으로 선형적으로 채운다
<img width="747" height="725" alt="image" src="https://github.com/user-attachments/assets/fc46dcc3-accb-44b1-9210-87c8cde5e650" />


공정 상 데이터는 시계열에 따라 물리적인 연속성을 갖기 때문이다.

<br />

### 인터랙티브 그래프 플롯
코드 실행 시 plotly 라이브러리 기반 인터랙티브 그래프가 플롯된다.
본 README 파일에서는 캡쳐이미지를 첨부하였다.
<img width="1668" height="450" alt="image" src="https://github.com/user-attachments/assets/2bb1ce55-63c3-4fa9-868a-f6f47e388a84" />
