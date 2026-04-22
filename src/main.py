from sensors.motion_sensor import detect_motion
from controller.light_control import control_light
import time

print("🚀 Smart Street Light System Started")

while True:
    motion = detect_motion()
    result = control_light(motion)
    
    print(result)
    
    time.sleep(3)  # 3 seconds delay
