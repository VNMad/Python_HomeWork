#____________________________________________________________________
#1. Воспроизведение мультимедиа
#____________________________________________________________________
class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Attribute 'audio_tracks' not found")

        result = [f"Воспроизведение аудио для {self.__class__.__name__}:"]

        for track in self.audio_tracks:
            result.append(track)

        return "\n".join(result)


class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError("Attribute 'video_files' not found")

        result = [f"Воспроизведение видео для {self.__class__.__name__}:"]

        for video in self.video_files:
            result.append(video)

        return "\n".join(result)


class MediaPlayer(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files


try:
    player = MediaPlayer(
        ["audio1.mp3", "audio2.mp3"],
        ["video1.mp4", "video2.mp4"]
    )

    print(player.play_audio())
    print()
    print(player.play_video())

except AttributeError as error:
    print(error)
#____________________________________________________________________
#2. Воспроизведение мультимедиа
#____________________________________________________________________
class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Attribute 'audio_tracks' not found")

        result = [f"Воспроизведение аудио для {self.__class__.__name__}:"]

        for track in self.audio_tracks:
            result.append(track)

        return "\n".join(result)


class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError("Attribute 'video_files' not found")

        result = [f"Воспроизведение видео для {self.__class__.__name__}:"]

        for video in self.video_files:
            result.append(video)

        return "\n".join(result)


class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files


tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]


try:
    player = MediaPlayer(tracks)
    laptop = Laptop(tracks, movies)

    print(player.play_audio())
    print(laptop.play_audio())
    print(laptop.play_video())

except AttributeError as error:
    print(error)