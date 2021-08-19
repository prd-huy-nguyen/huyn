import pyttsx3
import speech_recognition
robot_brain = "Tôi không hiểu, làm ơn nói lại"
engine = pyttsx3.init()
engine.say(robot_brain)
engine.runAndWait()

