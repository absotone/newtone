import musicalbeeps


"""
    Helper class to convert the generated output into a format suitable for musicalbeeps
"""
class SoundHelper:
    input_str = str 
    output_str = str 
    
    """
        Constructor
    """
    def __init__(self, input_str):
        self.input_str = input_str
        self.output_str = " "

        self.convert_musicalbeeps()
        
    """
        Converter algorithm
    """
    def convert_musicalbeeps(self):

        # Splitting the input string
        l = self.input_str.split(" ")

        output_list = []

        # Iterating through each note and changing the "sharp" notation
        for note in l:
            new_note = note
            if "♯" in note:
                new_note = note.replace("♯", "")
                new_note += "#"  
            output_list.append(new_note)

        self.output_str = " ".join(output_list)

    """
        Get Output String
    """
    def get_output_string(self):
        return self.output_str
    
"""
    Class to play the generated music
"""
class SoundPlayer:
    volume = float 
    play_time = float

    """
        Constructor
    """
    def __init__(self, volume = 0.5, play_time = 0.5):
        self.volume = volume
        self.player = musicalbeeps.Player(
            volume = self.volume,
            mute_output = False
        )
        self.play_time = play_time

    """
        Function to play sound 
            - Conversion into the appropriate format
            - Using the sound player to play each note one at a time
    """
    def play(self, input_str):

        # Getting the string with the converted notes
        helper = SoundHelper(input_str)
        play_str = helper.get_output_string()

        # Playing one note at a time
        l = play_str.split(" ")
        for note in l:
            self.player.play_note(note, self.play_time)