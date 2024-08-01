import subprocess
"""如何用python实现视频的自定义区域裁剪"""
input_video = "3 444.mp4"
output_video = "4.mp4"
w = 1000
h = 1080
x = 0
y = 0

def cut_video(input_video, output_video, x=0, y=0, w=1920, h=1080):
    # cmd = f'ffmpeg -i {input_video} -filter:v "crop={w}:{h}:{x}:{y}" {output_video}'
    cmd = f'ffmpeg -i "{input_video}" -filter:v "crop={w}:{h}:{x}:{y}" "{output_video}"'
    subprocess.run(cmd)

cut_video(input_video, output_video,x,y,w,h)