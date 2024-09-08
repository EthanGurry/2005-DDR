import mido

# dictionary for notes to direction
dictNotes = {48: 'down', 49:'left_down', 50:'left', 52:'left_up', 53:'up', 55:'right_up', 57:'right', 59:'right_down',
             60: 'down2', 61:'left_down2', 62:'left2', 64:'left_up2', 65:'up2', 67:'right_up2', 69:'right2', 71:'right_down2'}

# Load the MIDI file
midi_file = mido.MidiFile('song_test_V001.mid')

# Extract relevant information: (note, velocity, time in ticks)
notes = []
tempo = 521739.13  # Default tempo (120 BPM) if not set by a meta message
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
    arrow = dictNotes[note]
    return arrow

# Convert all note events to real-time values
for i in range(len(notes)):
    note, velocity, ticks = notes[i]
    time_in_seconds = ticks_to_seconds(ticks, tempo, ticks_per_beat)
    notes[i] = (note, convert_notes(note), velocity, time_in_seconds)
