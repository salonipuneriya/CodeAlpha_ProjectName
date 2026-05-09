import tkinter as tk
from tkinter import messagebox
import os

# Main window
root = tk.Tk()
root.title("AI Music Generator")
root.geometry("500x400")
root.config(bg="black")

# Title
title = tk.Label(
    root,
    text="AI Music Generator 🎵",
    font=("Arial", 22, "bold"),
    bg="black",
    fg="cyan"
)
title.pack(pady=20)

# Generate Music Function
def generate_music():
    os.system("python generate_music.py")
    messagebox.showinfo("Success", "Music Generated Successfully!")

# Play Music Function
def play_music():
    os.startfile("output.mid")

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Music",
    font=("Arial", 14),
    bg="cyan",
    command=generate_music
)
generate_btn.pack(pady=20)

# Play Button
play_btn = tk.Button(
    root,
    text="Play Music",
    font=("Arial", 14),
    bg="lightgreen",
    command=play_music
)
play_btn.pack(pady=20)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    font=("Arial", 14),
    bg="red",
    fg="white",
    command=root.destroy
)
exit_btn.pack(pady=20)

root.mainloop()