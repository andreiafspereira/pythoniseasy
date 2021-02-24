"""
PIRPLE PYTHON IS EASY
Homework #1: Variables
File name: main.py
Description: Python code with several types of meta-data to describe a song. The file will print the several attributes
"""

# The following attributes are string variables that indicate the name, the artist and the genre of the song
NameSong = "Theme from Jurassic Park"	
Artist = "John Williams"
Genre = "Soundtrack"
SubGenre = "Movie Soundtrack"
HowItSounds = "Epic"

# The following attributes are two integers variables that indicate the release year and duration of the song
TrackNumber = 2
YearReleased = 1993
DurationInSeconds = 60 * 3 + 27 # The music lasts 3minutes and 27 seconds. Therefore, 60 seconds * 3 + 27 seconds
#Other alternative could be a string variable: DurationInSeconds = "207" + " seconds" 
# This attribute is a float variable
DurationInMinutes = 3.45 # 27 / 60 seconds = 0.45 minutes + 3 minutes


# FINAL RESULT:
#String variables
print(NameSong)
print(Artist)
print(Genre)
print(SubGenre)
print(HowItSounds)
#Integer variables
print(TrackNumber)
print(YearReleased)
print(DurationInSeconds)
#Float variable
print(DurationInMinutes)