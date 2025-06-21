import cv2
import mediapipe as mp
from gesture_controller import detect_gesture
from media_controller import handle_action
import tkinter as tk
from PIL import Image, ImageTk

class GestureMediaPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Gesture Media Player")
        self.label = tk.Label(root, text="Gesture: None", font=("Helvetica", 16))
        self.label.pack()
        self.video_label = tk.Label(root)
        self.video_label.pack()
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.current_gesture = "None"
        self.update()

    def update(self):
        success, frame = self.cap.read()
        if not success:
            return
        frame = cv2.flip(frame, 1)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        action = None

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                gesture = detect_gesture(handLms)
                if gesture:
                    self.current_gesture = gesture
                    handle_action(gesture)
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)

        self.label.config(text=f"Gesture: {self.current_gesture}")
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)
        self.root.after(10, self.update)

    def on_closing(self):
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GestureMediaPlayerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()