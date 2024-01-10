


#Split an MP3 into shorter clips in a sub folder. Retain file date modified properties.

#For compatibility and backup purposes.
#Draft version-- Documentation, codes style and refactoring are works in progress.


#Output --creates a new folder, and mp3s in the new folder.
#        Output files are from splitting the source file into clips with length given in seconds.
#        Output files and folder retain the modification time of the source file.
#         output folder
#                  name based on the clip size and the source file
#                  location based on the source file
#Input -- Prompt user to select one mp3 file from a folder.
#Tested -- in python version python3.8

#notes before uploading to GitHub
#     remove/refactor the line about sys variables  sys.path.insert since it links to an absolute path to my pip installation modules
#     remove the above line and this
#     OP was using a line that looked like sys.path.insert(0, '/Users/path-to/python3.8/site-packages')





import sys

from pydub import AudioSegment
import os

import tkinter as tk
from tkinter import filedialog

seconds = 7

def open_file_dialog():
    # Create a file dialog and store the selected file's path
    file_path = filedialog.askopenfilename()

    # Print the selected file's path to the console
    if file_path:
        print("Selected file: " + os.path.basename(file_path) )
        #recog_speech_to_console(file_path)

        # Input MP3 file path

        #extract filename from path
        #inputmp3basename = os.path.basename(file_path)

       

        # Output directory for the chunks
        output_dir = file_path + f"_{seconds}sec_clips"

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Load the input MP3 file
        audio = AudioSegment.from_mp3(file_path)

        # Calculate the duration of a __- sec chunk in milliseconds
        chunk_duration = seconds * 1000  # 3 minutes in milliseconds

        # Get the modification time of the source file
        source_mod_time = os.path.getmtime(file_path)
        
        
        # Split the MP3 into 3-minute chunks
        for i, start_time in enumerate(range(0, len(audio), chunk_duration)):
            chunk = audio[start_time:start_time + chunk_duration]
            output_file = os.path.join(output_dir, f"clip_{i+1}.mp3")
            chunk.export(output_file, format="mp3")
            # Set the modification time of the destination file to match the source file
            os.utime(output_file, (source_mod_time, source_mod_time))
        os.utime(output_dir, (source_mod_time, source_mod_time))
            
                
     
        
    else:
        print("No file selected.")

# Create the main application window
root = tk.Tk()
root.title("File Chooser Example")

# Create a button to trigger the file dialog
button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack(pady=20)

# Start the main event loop
root.mainloop()
