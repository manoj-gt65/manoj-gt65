from sensors.motion_sensor import detect_motion

motion = detect_motion()

if motion:
    print("Light ON")
else:
    print("Light DIM")
