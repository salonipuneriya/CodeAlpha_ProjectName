from music21 import converter, instrument, note, chord
import glob

notes = []

for file in glob.glob("dataset/*.mid"):

    print("Reading File:", file)

    midi = converter.parse(file)

    parts = instrument.partitionByInstrument(midi)

    if parts:
        notes_to_parse = parts.parts[0].recurse()
    else:
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

print("\nTotal Notes Found:", len(notes))

print("\nFirst 20 Notes:")
print(notes[:20])