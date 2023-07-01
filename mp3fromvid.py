import moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip("C:\python\Practicum\SaveInsta.App - 3111054032582955337_59576455229.mp4")

print("conversion started")
audio = video.audio
audio.write_audiofile("harjot.mp3")
print("Successfully converted")