import RPi.GPIO as GPIO 
from time import sleep  

servoPin          = 12   
SERVO_MAX_DUTY    = 12   
SERVO_MIN_DUTY    = 3   

GPIO.setmode(GPIO.BOARD)        
GPIO.setup(servoPin, GPIO.OUT)  

servo = GPIO.PWM(servoPin, 50)  
servo.start(0)  
'''
서보 위치 제어 함수
degree에 각도를 입력하면 duty로 변환후 서보 제어(ChangeDutyCycle)
'''
def setServoPos(degree):
  # 각도는 180도를 넘을 수 없다.
  if degree > 180:
    degree = 180

  # 각도를 duty로 변경한다.
  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
  # duty 값 출력
  print("Degree: {} to {}(Duty)".format(degree, duty))

  # 변경된 duty값을 서보 pwm에 적용
  servo.ChangeDutyCycle(duty)

  #서보 작동 테스트용 코드
def main()
  # 서보 0도
  setServoPos(0)
  sleep(1) # 1초 대기
  
  # 90도
  setServoPos(90)
  sleep(1)
  
  # 50도
  setServoPos(50)
  sleep(1)

  # 120도
  setServoPos(120)
  sleep(1)

  # 180도
  setServoPos(180)
  sleep(1)

  servo.stop()
  GPIO.cleanup()
  
if __name__ == "__main__":  
  main()
  #실제 사용할 예정인 코드
  
import RPi.GPIO as GPIO 
from time import sleep  

servoPin          = 12   
SERVO_MAX_DUTY    = 12   
SERVO_MIN_DUTY    = 3   

GPIO.setmode(GPIO.BOARD)        
GPIO.setup(servoPin, GPIO.OUT)  

servo = GPIO.PWM(servoPin, 50)  
servo.start(0)  

def setServoPos(degree):
  if degree > 180:
    degree = 180

  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
  print("Degree: {} to {}(Duty)".format(degree, duty))

  servo.ChangeDutyCycle(duty)
  
def main()
  setServoPos(180)  #서보를 작동하여 고리를 걸수있게 위치를 조정
  sleep(물건이 정해진위치에 도달했을때까지)
  
  setServoPos(90)
  sleep(기체가 목표지점에 도착하기 전까지)
  
  setServoPos(180)    #고리에 걸려잇던 물건 낙하
  sleep(10)    #확실하게 물건이 낙하할때까지 대기
  
  servo.stop()
  GPIO.cleanup()
  
if __name__ == "__main__":  
  main()