from __future__ import print_function
from lxml import etree
import subprocess, time, signal, sys, os
from datetime import date

def save_xml(Elm, date, name, age, serial, gender):
    #CVCR=E.cvcr
    SUBJECT = Elm.subject
    DATE = Elm.date
    SERIAL = Elm.serial
    NAME = Elm.name
    AGE = Elm.age
    GENDER = Elm.gender
    the_doc=(SUBJECT(DATE(date),SERIAL(str(serial)),NAME(str(name)),AGE(str(age)),GENDER(str(gender)), ID=str(serial)))

    DOC = etree.tostring(the_doc, pretty_print=True)
    output_file = open( 'cvcr.xml', 'a' )
    output_file.seek(20)
    #output_file.write( '<?xml version="1.0"?>' )
    output_file.write(DOC)
    output_file.close()
    
def signal_handler(signal, frame):
    """Invokes when receives a signal.

    Args:
        signal (SIGINT): Type of signal.
        frame (int): Frame number.
    """
    time.sleep(1)
    print('Ctrl+C received in wrapper.py') 

def save_data(sleep_time, muse_command):
    """Saves data using the received shell command.

    Args:
        sleep_time (int): Halt the process to finish executing the shell command.
        muse_command (str): The shell command that is executed using python's `subprocess`.
    """
    command = muse_command
    signal.signal(signal.SIGINT, signal_handler)
    print('command Starting')
    subprocess.Popen(command)
    print('command started')
    time.sleep(sleep_time)
    print('Timeout Completed')
    os.kill(signal.CTRL_C_EVENT, 0)

def vid_player(media_player_path, video_path, matFileName):
    """Plays a video and saves the EEG data.
    When the Start button is pressed, it cals this function which uses system commands to automatically
    start a video and record the EEG data, and saves them to the working directory.

    Args:
        media_player_path (str): Path to the media player executable (preferred: VLC media player).
        video_path (str): Path to the video
        matFileName (str): Name of the mat file where all the EEG data will be dumped.
    """
    print(video_path)
    command= media_player_path +  " --fullscreen " + video_path #\"F:\Exp1.mp4\""
    muse_command="muse-player -l udp:5001 -M " + matFileName + ".mat"
    muse_command=str(muse_command)
    print(command)
    print(muse_command)
    #subprocess.Popen(muse_command)
    subprocess.Popen(command)
    time.sleep(1)
    save_data(5, muse_command)