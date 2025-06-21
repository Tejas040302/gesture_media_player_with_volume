def fingers_up(hand_landmarks):
    fingers = []
    # Thumb (check x for left or right hand)
    fingers.append(hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x)
    # Other fingers
    for tip_id in [8, 12, 16, 20]:
        fingers.append(hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y)
    return fingers