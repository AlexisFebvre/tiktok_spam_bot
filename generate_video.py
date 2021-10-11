from moviepy.editor import *
from random import shuffle

def generate_video():
    # define the image sequence
    image_sequence = ['assets/image.jpg']

    # make the clip
    clip = ImageSequenceClip(image_sequence, fps=1)
    clips = []

    for i in range(5):
        clips.append(clip)

    clips = concatenate_videoclips(clips)
    final_clip = CompositeVideoClip([clips])

    # export the final clip
    final_clip.write_videofile("assets/video/video.mp4", fps = 24)

def define_song_path():
    song = []
    for i in range(2):
        if i < 10:
            song.append(f"assets/music/0{i+1}.mp3")
        else:
            song.append(f"assets/music/{i+1}.mp3")
    shuffle(song)
    return song[0]

def add_effect_and_sound(song_path):
    videoclip = VideoFileClip("assets/video/video.mp4")
    audioclip = AudioFileClip(song_path)

    final_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = final_audioclip
    videoclip.write_videofile("assets/video/video.mp4")