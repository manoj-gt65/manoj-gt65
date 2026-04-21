from sensors.motion_sensor import detect_motion

motion = detect_motion()

if motion:
    print("🚶 Motion Detected → Light ON")
else:
    print("🌙 No Motion → Light DIM")
