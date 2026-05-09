from music21 import stream, note
import random

output_notes = []

# Notes for AI music generation
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

# Generate 50 random notes
for i in range(50):

    random_note = random.choice(notes)

    new_note = note.Note(random_note)

    new_note.quarterLength = 0.5

    output_notes.append(new_note)

# Create music stream
midi_stream = stream.Stream(output_notes)

# Save generated music
midi_stream.write('midi', fp='output.mid')

print("AI Generated Music Successfully!")