import random


class Audio:
    def __init__(self, title, url):  # Constructor
        self.title = title
        self.url = url
        self.ratings = []

    def add_rating(self, rating):  # Method to add rating
        self.ratings.append(rating)

    def average_rating(self):  # Method to Calculate average rating for the Audio Track
        if not self.ratings:
            return 0
        else:
            return sum(self.ratings) / len(self.ratings)


class PlayList:
    def __init__(self, name, genre):  # Constructor
        self.name = name
        self.genre = genre
        self.audio_tracks = []

    def add_audio(self, audio):  # Method to add Audio tracks
        self.audio_tracks.append(audio)

    def get_audio(self):  # Method to get the audio
        return self.audio_tracks

    def average_rating(self):  # Method to Calculate average rating for the Playlist
        if not self.audio_tracks:
            return 0
        else:
            total_rating = sum(audio.average_rating() for audio in self.audio_tracks)
            return total_rating / len(self.audio_tracks)


def generate_random_ratings():  # Method to generate Ratings in random from 0 to 5
    return [random.randint(0, 5) for _ in range(3)]


rock_playlist = PlayList("Rock Hits", "Rock")  # Create a new PlayList

# Add Audio Track to the PlayList
Audio1 = Audio("Song 1", "https://example.com/songA.mp3")
Audio2 = Audio("Song 2", "https://example.com/songB.mp3")
rock_playlist.add_audio(Audio1)
rock_playlist.add_audio(Audio2)

# Get/Print the Audio Tracks
for audio in rock_playlist.get_audio():
    print(f"Audio: {audio.title}, URL: {audio.url}")

# Generate Ratings for the Audio Tracks and Calculate the Average Rating for the PlayList
for audio in [Audio1, Audio2]:
    ratings = generate_random_ratings()
    for rating in ratings:
        audio.add_rating(rating)
print(f"Rating for {Audio1.title} is {Audio1.average_rating():.2f}")
print(f"Rating for {Audio2.title} is {Audio2.average_rating():.2f}")
print(f"Average rating for {rock_playlist.name} is {rock_playlist.average_rating():.2f}")
