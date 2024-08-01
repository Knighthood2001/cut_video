import tkinter as tk
from tkinter import filedialog
import subprocess
"""本版本需要在四个框输入内容"""
def cut_video(input_video, output_video, x=0, y=0, w=1920, h=1080):
    # 确保 x, y, w, h 是整数
    x, y, w, h = map(int, (x, y, w, h))
    cmd = f'ffmpeg -i "{input_video}" -filter:v "crop={w}:{h}:{x}:{y}" "{output_video}"'
    subprocess.run(cmd, shell=True)

def browse_input():
    # 弹出对话框选择输入视频文件
    global input_video
    input_video = filedialog.askopenfilename(title="Select Input Video", filetypes=[("Video files", "*.mp4 *.avi *.mov")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_video)

def browse_output():
    # 弹出对话框选择输出视频文件
    global output_video
    output_video = filedialog.asksaveasfilename(title="Select Output Video", filetypes=[("Video files", "*.mp4")], defaultextension=".mp4")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_video)

def execute_cut():
    # 执行裁剪视频的操作
    print(input_video, output_video)
    cut_video(input_video, output_video)

# 创建主窗口
root = tk.Tk()
root.title("Video Cutter")

# 输入文件路径输入框
input_label = tk.Label(root, text="Input Video Path:")
input_label.pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()
input_button = tk.Button(root, text="Browse", command=browse_input)
input_button.pack()

# 输出文件路径输入框
output_label = tk.Label(root, text="Output Video Path:")
output_label.pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
output_button = tk.Button(root, text="Browse", command=browse_output)
output_button.pack()

# 裁剪参数输入框
x_label = tk.Label(root, text="X:")
x_label.pack()
x_entry = tk.Entry(root, width=10)
x_entry.pack()
y_label = tk.Label(root, text="Y:")
y_label.pack()
y_entry = tk.Entry(root, width=10)
y_entry.pack()
w_label = tk.Label(root, text="Width:")
w_label.pack()
w_entry = tk.Entry(root, width=10)
w_entry.pack()
h_label = tk.Label(root, text="Height:")
h_label.pack()
h_entry = tk.Entry(root, width=10)
h_entry.pack()

# 裁剪按钮
cut_button = tk.Button(root, text="Cut Video", command=execute_cut)
cut_button.pack()

# 运行主循环
root.mainloop()