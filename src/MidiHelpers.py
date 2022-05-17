from mido import MidiFile
import sys 

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
            
