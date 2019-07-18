import time
import webbrowser

break_count=0
print("This program started on"+time.ctime())
while(break_count<3):
    time.sleep(60*30)
    webbrowser.open("https://www.youtube.com/watch?v=s7L2PVdrb_8")
    break_count=break_count+1
