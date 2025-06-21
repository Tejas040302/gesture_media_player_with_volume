import time

# Store previous Y position for comparison
last_y_position = None
last_action_time = 0

def detect_gesture(hand_landmarks):
    global last_y_position, last_action_time
    fingers = [hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x]  # Thumb
    for tip_id in [8, 12, 16, 20]:  # Other fingers
        fingers.append(hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y)

    current_time = time.time()

    # Volume control with Y-coordinate of middle finger tip
    y = hand_landmarks.landmark[12].y

    if last_y_position is not None:
        delta = y - last_y_position
        if abs(delta) > 0.05 and (current_time - last_action_time) > 0.5:
            last_action_time = current_time
            if delta < 0:
                return "volume_up"
            else:
                return "volume_down"

    last_y_position = y

    # Gesture-based actions
    if fingers == [0, 1, 0, 0, 0]:
        return "forward"
    elif fingers == [1, 0, 0, 0, 0]:
        return "backward"
    elif fingers == [0, 1, 1, 0, 0]:
        return "next"
    elif fingers == [0, 0, 1, 1, 0]:
        return "previous"
    elif fingers == [1, 1, 1, 1, 1]:
        return "pause"
    elif fingers == [0, 0, 0, 0, 0]:
        return "play"

    return None