import time
import webbrowser





total_breaks = 3
breaks_count = 0


print("the play time is " +time.ctime())
while (breaks_count < total_breaks) :
    time.sleep(5)
    webbrowser.open("http://www.youtube.com")
    breaks_count = breaks_count + 1
