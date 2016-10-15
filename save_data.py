import subprocess, time, signal, sys, os

def save_data(sleep_time):
    command = "muse-player -l udp:5001 -M output.mat"
    def signal_handler(signal, frame):
      time.sleep(1)
      print 'Ctrl+C received in wrapper.py'

    signal.signal(signal.SIGINT, signal_handler)
    print 'command Starting'
    subprocess.Popen(command)
    print 'command started'
    time.sleep(sleep_time)
    print 'Timeout Completed'
    os.kill(signal.CTRL_C_EVENT, 0)
