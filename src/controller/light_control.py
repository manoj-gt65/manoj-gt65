def control_light(motion):
    if motion:
        return "🚶 Motion Detected → Light ON (High Brightness)"
    else:
        return "🌙 No Motion → Light DIM (Energy Saving Mode)"
