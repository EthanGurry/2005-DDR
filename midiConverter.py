import mido

# Load the MIDI file
midi_file = mido.MidiFile('midi_test_02_fixed.mid')

# Extract relevant information: (note, velocity, time in ticks)
notes = []
tempo = 500000  # Default tempo (120 BPM) if not set by a meta message
ticks_per_beat = midi_file.ticks_per_beat  # PPQ (Pulses Per Quarter note)

for track in midi_file.tracks:
    absolute_time = 0
    for msg in track:
        absolute_time += msg.time  # accumulate delta times into absolute time
        if msg.type == 'set_tempo':
            tempo = msg.tempo
        if msg.type == 'note_on' and msg.velocity > 0:
            notes.append((msg.note, msg.velocity, absolute_time))


# Convert ticks to time in seconds
def ticks_to_seconds(ticks, tempo, ticks_per_beat):
    return (ticks / ticks_per_beat) * (tempo / 1000000)

# convert note to direction, p1 has lower octave
def convert_notes(note):
    arrow = ''
    if note == 49:
        arrow = 'left_down'
    elif note == 61:
        arrow = 'left_down2'
    elif note == 50:
        arrow = 'left'
    elif note == 62:
        arrow = 'left2'
    elif note == 52:
        arrow = 'left_up'
    elif note == 64:
        arrow = 'left_up2'
    elif note == 53:
        arrow = 'up'
    elif note == 65:
        arrow = 'up2'
    elif note == 55:
        arrow = 'right_up'
    elif note == 67:
        arrow = 'right_up2'
    elif note == 57:
        arrow = 'right'
    elif note == 69:
        arrow = 'right2'
    elif note == 59:
        arrow = 'right_down'
    elif note == 71:
        arrow = 'right_down2'
    if note == 60:
        arrow = 'down'
    elif note == 72:
        arrow = 'down2'
    return arrow

# Convert all note events to real-time values
for i in range(len(notes)):
    note, velocity, ticks = notes[i]
    time_in_seconds = ticks_to_seconds(ticks, tempo, ticks_per_beat)
    notes[i] = (note, convert_notes(note), velocity, time_in_seconds)