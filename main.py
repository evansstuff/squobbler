# Squobbler by Evan Truong: stitch a bunch of audio files together in a random sequence
# Requires ffmpeg installed
# Run on desktop - Do not run in online IDE

import ffmpeg
import random
import tkinter
from datetime import datetime
from tkinter.filedialog import askopenfilenames

# make list to hold filenames
list_files = []

root = tkinter.Tk()
root.withdraw()
print("evan's squobbler 2025: stitch a bunch of audio files together in a random sequence")

while True:
    print("Type 1 to add sample(s) to squobbler. Type 2 to render and export as wav")
    user_sel = input("Select: ")

    if user_sel == "1":
        # open file selector dialog
        root.attributes("-topmost", True)
        filenames = askopenfilenames(parent=root, filetypes=[("Audio files", ".mp3 .wav .flac .aac .ogg .aiff .aif")])

        # add to file list
        for item in filenames:
            list_files.append(str(item))
        print(str(filenames) + " added")

    elif user_sel == "2":
        if not list_files:
            print("No audio files selected")
        else:
            user_sample_count = int(input("How many samples long would you like the exported file to be? "))

            # concat audio files
            file_output = "squobbler_" + str(datetime.today().strftime('%Y-%m-%d %H%M%S')) + ".wav"
            input_streams = [ffmpeg.input(f) for f in random.choices(list_files, k=user_sample_count)]
            concat_audio = ffmpeg.concat(*input_streams, v=0, a=1)
            ffmpeg.output(concat_audio, file_output).run()
            print("Squobbling done. Exported to " + file_output)

    else:
        print("Invalid selection. Please select 1 or 2")