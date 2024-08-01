import tkinter as tk
from tkinter import filedialog
import subprocess
import threading

"""本版本添加一个记录之前输入裁剪框位置的"""""
def cut_video(input_video, output_video, event, x=0, y=0, w=1920, h=1080):
    # 确保 x, y, w, h 是整数
    x, y, w, h = map(int, (x, y, w, h))
    cmd = f'ffmpeg -i "{input_video}" -filter:v "crop={w}:{h}:{x}:{y}" "{output_video}"'
    subprocess.run(cmd, shell=True)
    event.set()

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
    result_label.config(text="")
    # 从输入框中获取值并解析
    crop_values = crop_entry.get()
    try:
        # 假设使用逗号分隔 x, y, w, h
        x, y, w, h = map(int, crop_values.split(','))
    except ValueError:
        # 如果转换失败，给出错误提示
        result_label.config(text="Error: Please enter crop values in the format 'x,y,w,h'", fg="red")
        return
    # 创建一个Event对象
    event = threading.Event()
    # 创建线程
    thread = threading.Thread(target=cut_video, args=(input_video, output_video, event, x, y, w, h))

    # 启动线程
    thread.start()

    # 在主线程中等待事件变为“set”状态
    event.wait()
    # 事件被设置后，更新结果标签
    result_label.config(text="Cutting complete!", fg="green")

    # Save the last input to a text file
    with open('last_input.txt', 'w') as f:
        f.write(crop_entry.get())

def load_last_input():
    try:
        with open('last_input.txt', 'r') as f:
            last_input = f.read().strip()
            crop_entry.delete(0, tk.END)
            crop_entry.insert(0, last_input)
    except FileNotFoundError:
        pass  # 如果文件不存在，不执行任何操作

# 创建主窗口
root = tk.Tk()
root.title("视频裁剪助手 by公众号：认知up吧")
# 设置窗口大小
root.geometry("400x300")


# 输入文件路径输入框
input_label = tk.Label(root, text="Input Video Path:")
input_label.pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()
input_button = tk.Button(root, text="选择", command=browse_input)
input_button.pack()

# 输出文件路径输入框
output_label = tk.Label(root, text="Output Video Path:")
output_label.pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
output_button = tk.Button(root, text="选择", command=browse_output)
output_button.pack()

# 裁剪参数输入框
crop_label = tk.Label(root, text="裁剪参数(x,y,w,h):")
crop_label.pack()
crop_entry = tk.Entry(root, width=20)
crop_entry.pack()

# 结果显示标签
result_label = tk.Label(root, text="", fg="black")
result_label.pack()

# 裁剪按钮
cut_button = tk.Button(root, text="裁剪", command=execute_cut)
cut_button.pack()

# Load last input on startup
load_last_input()

# 运行主循环
root.mainloop()

