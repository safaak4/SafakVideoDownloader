import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
import urllib.request
import datetime, ffmpeg, subprocess
from moviepy.editor import *
from pytube import YouTube

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Link:')
        #self.nameLabel.setFont()
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(600, 32)
        self.nameLabel.move(20, 30)

        pybutton = QPushButton('Send', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(75, 32)
        pybutton.move(690,20)


        self.show()

    def clickMethod(self):
        if self.line.text() != "":
            yt = YouTube(self.line.text())

            videoNameLabel = QLabel(self)
            videoNameLabel.move(15,70)
            videoNameLabel.setText(yt.title)
            videoNameLabel.setStyleSheet("font: 14pt Arial")
            videoNameLabel.show()

            videoAuthorLabel = QLabel(self)
            videoAuthorLabel.move(15, 100)
            videoAuthorLabel.setText(yt.author)
            videoAuthorLabel.setStyleSheet("font: 10pt Arial")
            videoAuthorLabel.show()

            urllib.request.urlretrieve(yt.thumbnail_url, 'thumbnail.jpeg')
            photo = QLabel(self)
            photo.setText("")
            pixmap = QPixmap('thumbnail.jpeg')
            photo.setPixmap(pixmap)
            photo.resize(480,270)
            #photo.resize(pixmap.width(), pixmap.height())
            photo.setScaledContents(True)
            photo.move(155,130)
            photo.show()

            videoDurationLabel = QLabel(self)
            videoDurationLabel.move(580, 402)
            videoDurationLabel.setText(str(datetime.timedelta(seconds=yt.length)))
            videoDurationLabel.setStyleSheet("font: 10pt Arial")
            videoDurationLabel.show()



            stream = yt.streams.filter(resolution='1080p').filter(mime_type='video/mp4').first()
            voice = yt.streams.filter(mime_type='audio/mp4').first()
            if str(stream.url) != "" and str(voice.url) != "" :
                pybutton1080 = QPushButton('1080p', self)
                pybutton1080.resize(75,35)
                pybutton1080.move(20, 435)
                pybutton1080.show()
               # stream.download("", "video")
                #voice.download("", "soundd")

                video = VideoFileClip(os.path.join("path", "to", "soundd.mp4"))
                video.audio.write_audiofile(os.path.join("path", "to", "movie_sound.mp3"))

               # infile1 = ffmpeg.input("video.mp4")
                #infile2 = ffmpeg.input("movie_sound.mp3")

                #merged = ffmpeg.concat(infile1, infile2, v=1, a=1)
                #output = ffmpeg.output(merged[0], merged[1], "merged.mp4")




                #clip1 = VideoFileClip("videoo.mp4")
                #clip2 = VideoFileClip("voicee.mp4")
                #clip2.audio.write_audiofile("sound.mp3")

                #new_video = clip1.set_audio(clip2.audio)
                #new_video.write_videofile("outputVideo.mp4")

                #final_clip = concatenate_videoclips([clip1, clip2])
                #final_clip.write_videofile("my_concatenation.mp4")




                #subprocess.run("ffmpeg -i videoo.mp4 -i voicee.webm -c:v copy -c:a copy output.mp4")
                #subprocess.run("ffmpeg -i videoo.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate1.ts")
                #subprocess.run("ffmpeg -i voicee.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate2.ts")
                #subprocess.run('ffmpeg -i "concat:intermediate1.ts|intermediate2.ts" -c copy -bsf:a aac_adtstoasc output.mp4')
                #video = ffmpeg.input('videoo.mp4')
                #audio = ffmpeg.input('voicee.mp4')
                #ffmpeg.output(video, audio, 'out.mp4').run()
                #ffmpeg.concat(ffmpeg.input('videoo.mp4'), ffmpeg.input('voicee.mp4'), v=1, a=1).output('vidyo.mp4').run()
        else:
            print("Bir link giriniz!")


        #for i in yt.streams:
         #   print(i)
        # print(f"Video Başlığı: {yt.title}")
        # print(f"Video Sahibi: {yt.author}")
        # print(f"Thumbnail Resmi: {yt.thumbnail_url}")
        # print(f"Video Uzunluğu: {yt.length}")
        # print(f"Video Rating: {yt.rating}")
        # print(f"İzlenme Sayısı: {yt.views}")
        # print("*" * 30)
        # print(f"Video Açıklaması: {yt.description}")
        # print("*" * 30)


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("Safak Video Downloader")
pencere.setFixedSize(800,600)
sys.exit(app.exec_())