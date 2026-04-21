from sensors.motion_sensor import detect_motion
from controller.light_control import control_light

motion = detect_motion()

result = control_light(motion)

print(result)
