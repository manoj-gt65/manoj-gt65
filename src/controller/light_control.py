def control_light(motion):
    if motion == 0:
        return "🌙 No Motion → Light OFF"
    elif motion <= 3:
        return "💡 Low Motion → Dim Light"
    elif motion <= 7:
        return "🔆 Medium Motion → Medium Brightness"
    else:
        return "🚨 High Motion → Full Brightness"
