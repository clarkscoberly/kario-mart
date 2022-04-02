import os
import pathlib
import pyray


class AudioService():
    """A Raylib implementation of AudioService."""

    def __init__(self):
        self._sounds = {}
        
    def initialize(self):
        pyray.init_audio_device()
        
    def load_sounds(self, directory):
        filepaths = self._get_filepaths(directory, [".wav", ".mp3", ".wma", ".aac"])
        for filepath in filepaths:
            sound = pyray.load_sound(filepath)
            print('\n\n', filepath, '\n\n')
            self._sounds[filepath] = sound

    # Pass the filename with audio that you want played
    def play_sound(self, filename):
        sound = self._sounds[filename]
        pyray.play_sound(sound)
    
    def release(self):
        pyray.close_audio_device()
        
    def unload_sounds(self):
        for sound in self._sounds.values():
            pyray.unload_sound(sound)
        self._sounds.clear()
        
    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths