import random
import pandas as pd
from datetime import datetime, timedelta

# จำนวนบรรทัดข้อมูลที่ต้องการสร้าง
num_rows = 500

# วันเริ่มต้น
start_date = datetime(2024, 9, 1, 0, 0, 0)

# สร้างข้อมูล PM2.5 พร้อมกับอุณหภูมิและความชื้นสัมพัทธ์
data = []
for i in range(num_rows):
    # สุ่มค่า PM2.5 โดยมี 95% ของข้อมูลเป็นค่าระหว่าง 0-150
    if random.random() < 0.95:
        pm25_value = random.uniform(0, 150)  # ค่าปกติสำหรับ PM2.5
    else:
        pm25_value = random.uniform(150, 500)  # ค่าสูงมากสำหรับ PM2.5
    
    # สร้างข้อมูลอุณหภูมิและความชื้นสัมพัทธ์
    temperature = random.uniform(15, 40)  # อุณหภูมิใน °C
    humidity = random.uniform(30, 90)  # ความชื้นสัมพัทธ์ใน %
    
    # สร้างเวลาที่เพิ่มขึ้นทีละ 1 ชั่วโมง
    timestamp = start_date + timedelta(hours=i)
    
    # เพิ่มข้อมูลในลิสต์
    data.append([timestamp, pm25_value, temperature, humidity])

# สร้าง DataFrame จากข้อมูล
df = pd.DataFrame(data, columns=['Timestamp', 'PM2.5', 'Temperature', 'Humidity'])

# คำนวณหาค่าสูงสุดและต่ำสุดของ PM2.5
max_pm25 = df['PM2.5'].max()
min_pm25 = df['PM2.5'].min()

# แสดงผลลัพธ์ค่าสูงสุดและต่ำสุด


# ดึงข้อมูลของแถวที่มีค่า PM2.5 มากที่สุด
max_pm25_row = df.loc[df['PM2.5'] == max_pm25]
min_pm25_row = df.loc[df['PM2.5'] == min_pm25]
# แสดงข้อมูลทั้งหมดของแถวที่มีค่า PM2.5 มากที่สุด
print("\nข้อมูลทั้งหมดของค่า PM2.5 ที่มากที่สุด:")
print(max_pm25_row)
print("\nข้อมูลทั้งหมดของค่า PM2.5 ที่น้อยที่สุด:")
print(min_pm25_row)

# บันทึกข้อมูลลงไฟล์ CSV (ถ้าต้องการ)
df.to_csv('pm25_data.csv', index=False)

# แสดงข้อมูลตัวอย่าง 10 แถวแรก

