import pandas as pd
import numpy as np


# ------------------------Virtual FDC Sensor Data Load Process---------------------
# FDC data load (Csv file)
try : 
    df = pd.read_csv("virtual_fdc_sensor.csv")
    print("Successfully loaded FDC dataset.")

# FDC data generate (basic dataset)
except FileNotFoundError:
    print("Dataset not found. Generating dummy dataset for testing...")
    # 더미 데이터 생성 logic(실제 파일 없을 때를 대비한 방어코드)
    np.random.seed(42) # Random Data Generating
    rows = 1000
    df = pd.DataFrame({
        "Run_ID": np.repeat(np.arange(1, 11), 100),
        "Step_No": [1, 2, 3, 4, 5] * 200,
        "Pressure": 150.0 + np.random.normal(0, 1.5, rows),
        "RF_Power": 600.0 + np.random.normal(0, 4, rows),
        "Temp_He_Focus": 80.0 + np.random.normal(0, 0.8, rows),
        "Defect_Label": np.random.choice([0, 1], size=rows, p=[0.97, 0.03])
    })
#------------------------------------------------------------------------------------


# ------------------------Data Basic Structure(Shape) Print -------------------------
print("\n--- Data Shape ---")
print(df.shape)
#------------------------------------------------------------------------------------


# -------------------Sensor Data Average by Process RCP Step No.----------------------
print("\n--- Step-wise Sensor Mean Summary ---")
step_summary = df.groupby("Step_No")[["Pressure", "RF_Power", "Temp_He_Focus"]].mean()
print(step_summary)
#------------------------------------------------------------------------------------


# ---------------------------------null data check------------------------------------
null_ratio = df.isnull().mean() * 100
print("\n--- Missing Data Ratios (%) ---")
print(null_ratio)
#------------------------------------------------------------------------------------

