from mido import MidiFile
import sys 

"""
    Data Structure to store temporal data
"""
class TimeStore:

    velocity = int 
    time = int 
    note = int 

    """
        Constructor
    """
    def __init__(self, velocity, time, note):
        self.velocity = velocity 
        self.time = time 
        self.note = note 



"""
    Helper class to deal with operations on MIDI files
"""
class MidiHelpers:

    midi_obj = None

    """
        Constructor
    """ 
    def __init__(self, midi_file_path, clip = True):
        

        try:
            # Load the MIDI file
            self.midi_obj = MidiFile(midi_file_path, clip=clip)
        except Exception as e:
            print(f"Error in reading the MIDI file: {e}")
            sys.exit()
        
    """
        Extract Right Hand Notes' Track Information
    """
    def get_rhs_track(self):

        current_track = None 
        
        if self.midi_obj is None:
            print(f"No object specified")
            sys.exit() 

        try:
            # Search for "Piano right" track
            for track in self.midi_obj.tracks:
                for m in track:
                    if m.type == "track_name" and m.name == "Piano right":
                        current_track = track 
                        break

            return current_track 

        except Exception as e:
            print(f"Error in printing track information: {e}")
            sys.exit()

    """
        Get the list of temporal data points by using the TimeStore class 
    """
    def get_points_list_note_on(self):
        
        # Get the corresponding track 
        rhs_track = self.get_rhs_track()

        temp_list = []

        for message in rhs_track:
            # Look for all messages of the type "note_on"
            if message.type == "note_on":
                time = message.time 
                velocity = message.velocity
                note = message.note 

                # Store the object if its velocity > 0
                if velocity > 0:
                    ts = TimeStore(
                        velocity=velocity,
                        time=time,
                        note=note
                    ) 
                    temp_list.append(ts)

        return temp_list 
