import time
import board
import pwmio
from adafruit_motor import servo

pwm1 = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)

s1 = servo.Servo(pwm1)
s2 = servo.Servo(pwm2)

time.sleep(15)

for a in range(0, 181, 5):
    s1.angle = a
    time.sleep(0.05)

s1.angle = None

time.sleep(1)

for a in range(180, -1, -5):
    s2.angle = a
    time.sleep(0.05)

s2.angle = None
