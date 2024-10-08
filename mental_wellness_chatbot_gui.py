# mental_wellness_chatbot_gui.py

import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog  # Add simpledialog here
import datetime

# Simple database to store mood entries
mood_entries = []

class MentalWellnessChatbot:
    def __init__(self, master):
        self.master = master
        self.master.title("Mental Wellness Chatbot")

        self.chat_frame = tk.Frame(master)
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_area = scrolledtext.ScrolledText(self.chat_frame, state='disabled', wrap=tk.WORD, width=50, height=20)
        self.chat_area.pack()

        self.user_input = tk.StringVar()
        self.input_field = tk.Entry(self.chat_frame, textvariable=self.user_input, width=40)
        self.input_field.bind("<Return>", self.process_input)
        self.input_field.pack(pady=5)

        self.send_button = tk.Button(self.chat_frame, text="Send", command=self.process_input)
        self.send_button.pack(pady=5)

    def append_chat(self, message, sender="You"):
        """Append messages to the chat area."""
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def track_mood(self, mood):
        """Tracks the user's mood with a timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mood_entries.append({"mood": mood, "timestamp": timestamp})
        self.append_chat(f"Mood recorded: {mood}")

    def guided_breathing(self):
        """Provides a guided breathing exercise."""
        breathing_exercise = (
            "Inhale deeply through your nose for 4 seconds...\n"
            "Hold your breath for 4 seconds...\n"
            "Exhale slowly through your mouth for 4 seconds...\n"
            "Repeat this 3 times."
        )
        self.append_chat(breathing_exercise, sender="Chatbot")

    def journaling_prompt(self):
        """Provides a journaling prompt."""
        prompts = [
            "What are three things you are grateful for today?",
            "Describe a happy memory.",
            "What is one challenge you faced today, and how did you overcome it?",
            "How do you feel right now? Write about your emotions.",
        ]
        prompt = prompts[datetime.datetime.now().second % len(prompts)]
        self.append_chat(f"Prompt: {prompt}", sender="Chatbot")

    def show_mood_log(self):
        """Displays the logged moods."""
        if not mood_entries:
            self.append_chat("No mood entries found.", sender="Chatbot")
        else:
            log = "\n".join([f"{entry['timestamp']}: {entry['mood']}" for entry in mood_entries])
            self.append_chat(f"Mood Log:\n{log}", sender="Chatbot")

    def process_input(self, event=None):
        """Processes the user input."""
        user_message = self.user_input.get()
        if user_message.strip():
            self.append_chat(user_message)

            user_message = user_message.lower()

            if "track mood" in user_message:
                mood = simpledialog.askstring("Mood Tracker", "How are you feeling? (happy, sad, anxious, etc.):")
                if mood:
                    self.track_mood(mood)
            elif "guided breathing" in user_message:
                self.guided_breathing()
            elif "journaling" in user_message:
                self.journaling_prompt()
            elif "mood log" in user_message:
                self.show_mood_log()
            elif "bye" in user_message:
                self.append_chat("Goodbye! Take care of your mental health!", sender="Chatbot")
                self.master.quit()
            else:
                self.append_chat("I'm here to support your mental wellness. You can ask me to track your mood, guide you in breathing exercises, provide journaling prompts, or show your mood log.", sender="Chatbot")

        self.user_input.set("")  # Clear the input field


if __name__ == "__main__":
    root = tk.Tk()
    chatbot = MentalWellnessChatbot(root)
    root.mainloop()
