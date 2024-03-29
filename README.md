[![header](https://capsule-render.vercel.app/api?type=venom&height=300&color=0:038C7F,45:04BF8A,60:04D98B,100:74BF04&text=JMS%20Smart%20Farm&fontAlign=50&fontColor=ffffff&textBg=false&desc=By%20JMS.HW%20:%20qwer9679,%20CutTheWire&descAlign=50&descAlignY=63&fontAlignY=46)](https://github.com/CutTheWire/JMS_smart_farm.git)

## 🏷️ 스마트팜 메인 프로젝트 깃허브
[![스마트팜 프로젝트](https://capsule-render.vercel.app/api?type=waving&height=300&color=0:038C7F,30:04BF8A,70:04D98B,100:74BF04&text=Smart%20Farm%20Main&fontColor=ffffff&textBg=false&desc=Link%20:%20jgkim14_SmartFarm.git&descAlignY=53&fontAlignY=35&descAlign=67)](https://github.com/jgkim14/SmartFarm.git)

---

## 🌳 프로젝트 파일 트리
📦JMS_smart_farm  
 ┣ 📂Ar  
 ┃ ┗ 📂Arduino_UNO  
 ┃ㅤㅤ┗ 📂JMS_Arduino  
 ┃ㅤㅤㅤㅤ┗ 📜[JMS_Arduino.ino](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Ar/Arduino_UNO/JMS_Arduino/JMS_Arduino.ino)  
 ┃  
 ┣ 📂DB  
 ┃ ┗ 📂20240213  
 ┃ㅤㅤ┣ 📜[JMSPlant.db](https://github.com/CutTheWire/JMS_smart_farm/blob/main/DB/20240213/JMSPlant.db)  
 ┃ㅤㅤ┗ 📜[JMSPlant_remake.db](https://github.com/CutTheWire/JMS_smart_farm/blob/main/DB/20240213/JMSPlant_remake.db)  
 ┃  
 ┣ 📂Py  
 ┃ ┣ 📂Arduino  
 ┃ ┃ ┣ 📜[Ar_serial.py](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Py/Arduino/Ar_serial.py)  
 ┃ ┃ ┣ 📜[USB_cam.py](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Py/Arduino/USB_cam.py)  
 ┃ ┃ ┗ 📜[USB_device.py](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Py/Arduino/USB_device.py)  
 ┃ ┃  
 ┃ ┣ 📂DATA  
 ┃ ┃ ┣ 📜[DB_Remaker.py](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Py/DATA/DB_Remaker.py)  
 ┃ ┃ ┗ 📜[DB_to_chart.py](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Py/DATA/DB_to_chart.py)  
 ┃ ┃  
 ┃ ┗ 📂TEST  
 ┃ㅤㅤ┣ 📜[thread_py.py](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Py/TEST/thread_py.py)  
 ┃ㅤㅤ┗ 📜[v4l2_cam_list.py](https://github.com/CutTheWire/JMS_smart_farm/blob/main/Py/TEST/v4l2_cam_list.py)  
 ┃  
 ┣ 📜.gitignore  
 ┗ 📜README.md  

---

## ⚡ 스마트팜 전력 배선 시스템
   <table> 
      <tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=13ar-wA-7TMwUxgA23lSkwvVG2YBkz0Jr" width="100%"></td>
      <tr> 
      </tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=16K5b2SZef0kbdzVoox6DTChH2M7OzhQk" width="100%"></td>
      </tr> 
   </table>
   
   ## ⬇️ 전선배선도면.eddx
   [![스마트팜 프로젝트](https://drive.google.com/uc?export=view&id=16YLoCCLto-hLLAYDK2dCux5KVayjZyTT)](https://drive.google.com/file/d/16HMf_8yOA0kCh1TgKVcjFiXK0HJdRApW/view?usp=sharing) 
   
---
   
## 📑 하드웨어 프로젝트 일지

### 🔖 24.01.26. 제작
**`프로젝트 준비와 제품 초기 구현`**
- 🖼️ 제품 사진
   <table> 
      <tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=13nXrkL33pT9uBIrKXoJrSGe4aOVKN_0u" width="100%"></td>
         <td><img src="https://drive.google.com/uc?export=view&id=144tk6avxZNa4_HuzkyqxFrZhR9xbo1h8" width="100%"></td>
      </tr> 
      <tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=14Ogi2ysVYqVO2q12Cxmg59WsElty5bQ0" width="100%"></td>
         <td><img src="https://drive.google.com/uc?export=view&id=13uQe_D5V6Vn22UHL7goNzCJvzEg53_kq" width="100%"></td>
      </tr> 
   </table>
   
### 🔖 24.02.15. 업데이트
**`프로젝트 시작과 초기 기능 구현`**
- 아두이노(Ar): 펌프, 시스템 팬, LED를 릴레이 모듈로 제어하고, 토양습도와 대기 온습도 데이터를 PC로 전송하는 기능 구현
- 파이썬(Py): 아두이노로부터 받은 데이터를 전처리하고 릴레이 모듈을 제어할 수 있는 코드 작성
- 데이터베이스(DB): 아두이노로부터 받은 데이터를 파이썬을 통해 .DB 확장자 파일로 저장
- 🖼️ 제품 사진
   <table> 
      <tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=13hmXm9q-x0pQnWn0C0wjOHo7t0IL7lk2" width="100%"></td> 
         <td><img src="https://drive.google.com/uc?export=view&id=13i56eYeBd5VBV6YraZ1dXHlAZf_3Xk6A" width="100%"></td> 
      </tr> 
      <tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=13qgIXqM7vBqzyXxmizOYfaGgQFW42agh" width="100%"></td> 
         <td><img src="https://drive.google.com/uc?export=view&id=14zYG7T70KisGZ1m65AzTxvDTOlSMxEH4" width="100%"></td> 
      </tr> 
   </table>

- 🎞️ 제품 영상
  <table> 
     <tr> 
        <td><a href="https://youtu.be/A4H0RPvCFv8"><img src="http://img.youtube.com/vi/A4H0RPvCFv8/0.jpg" width="100%"></a></td> 
        <td><a href="https://youtu.be/YNV4qOM-Ld0"><img src="http://img.youtube.com/vi/YNV4qOM-Ld0/0.jpg" width="100%"></a></td> 
     </tr> 
     <tr> 
        <td><a href="https://youtu.be/Wl-SsZUtTho"><img src="http://img.youtube.com/vi/Wl-SsZUtTho/0.jpg" width="100%"></a></td> 
        <td></td> 
     </tr> 
  </table>
   
### 🔖 24.03.11. 업데이트
**`제품 기능 추가 및 수정`**
- 아두이노(Ar): 온습도 데이터를 OLED 디스플레이에 출력하는 기능 추가
- 파이썬(Py): USB 클래스 분리 및 카메라 코드와 시리얼 코드 수정
- 🖼️ 제품 사진
   <table> 
      <tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=15B5EbrdnA6jyz5gmvjj9xaWWKY4uvRn2" width="100%"></td> 
      <tr> 
      </tr>
         <td><img src="https://drive.google.com/uc?export=view&id=15lUDmlrBODD5llfT7j13NlH91uyC1SxP" width="100%"></td> 
      </tr> 
   </table>

### 🔖 24.03.18. 업데이트
**`제품 기능 추가 및 수정`**
- 아두이노(Ar): 데이터 송수신 코드 수정(LED, 시스템팬)
- 파이썬(Py): 시리얼 코드를 멀티쓰레드로 분산처리하는 기능 추가

### 🔖 24.03.24. 업데이트
**`제품 기능 수정`**
- 파이썬(Py): 라즈베리파이 우분투 OS에서 작동하도록 라이브러리 및 코드 수정
- 🖼️ 기능 사진
   <table> 
      <tr> 
         <td><img src="https://drive.google.com/uc?export=view&id=1Zk3cf9SlDXYjIp0twA4vFQgXR4xKxmK2" width="100%"></td>
      </tr> 
   </table>
