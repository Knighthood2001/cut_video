import tkinter as tk
from tkinter import filedialog
import subprocess
"""本版本直接在一个框输入四个参数"""
def cut_video(input_video, output_video, x=0, y=0, w=1920, h=1080):
    # 确保 x, y, w, h 是整数
    x, y, w, h = map(int, (x, y, w, h))
    cmd = f'ffmpeg -i "{input_video}" -filter:v "crop={w}:{h}:{x}:{y}" "{output_video}"'
    subprocess.run(cmd, shell=True)

def browse_input():
    # 弹出对话框选择输入视频文件
    global input_video
    input_video = filedialog.askopenfilename(title="Select Input Video",
                                             filetypes=[("Video files", "*.mp4 *.avi *.mov")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_video)


def browse_output():
    # 弹出对话框选择输出视频文件
    global output_video
    output_video = filedialog.asksaveasfilename(title="Select Output Video",
                                                filetypes=[("Video files", "*.mp4")],
                                                defaultextension=".mp4")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_video)

def execute_cut():
    # 从输入框中获取值并解析
    crop_values = crop_entry.get()
    try:
        # 假设使用逗号分隔 x, y, w, h
        x, y, w, h = map(int, crop_values.split(','))
    except ValueError:
        # 如果转换失败，给出错误提示
        result_label.config(text="Error: Please enter crop values in the format 'x,y,w,h'", fg="red")
        return

    # 执行裁剪操作
    cut_video(input_video, output_video, x, y, w, h)
    result_label.config(text="Cutting complete!", fg="green")


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
crop_label = tk.Label(root, text="Crop values (x,y,w,h):")
crop_label.pack()
crop_entry = tk.Entry(root, width=20)
crop_entry.pack()

# 结果显示标签
result_label = tk.Label(root, text="", fg="black")
result_label.pack()

# 裁剪按钮
cut_button = tk.Button(root, text="Cut Video", command=execute_cut)
cut_button.pack()

# 运行主循环
root.mainloop()