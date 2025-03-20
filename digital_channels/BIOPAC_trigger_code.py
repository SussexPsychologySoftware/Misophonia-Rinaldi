#2 Digits Hex code for each channel setting - see digital_channels.csv for channel combinations
'00' # all closed
'01' # BIOPAC channel 20
'02' # BIOPAC channel 21
'04' # BIOPAC channel 22
'08' # BIOPAC channel 23
'10' # BIOPAC channel 24
'20' # BIOPAC channel 25
'40' # BIOPAC channel 26
'80' # BIOPAC channel 27
'RR' # Reset port

#insert this at the beginning of the experiment code
import serial
# check port in device list
ser = serial.Serial("COM4", 115200, timeout=1, bytesize=8, stopbits=1) # This must always be used before sending any triggers, it specifies the settings for the serial port. Exact settings should be customised to your specific port 
ser.open # Open the port
ser.write('RR'.encode()) # Reset the port so that its ready for the first trigger    

# If you just wanted to use the hex code you could write the following to send a trigger:
# If using Psychopy then this could be inserted in the "Begin Routine" tab to send a trigger when a routine starts.
ser.write('80'.encode()) # Turn on BIOPAC channel 27
#if looking for a single spike
core.wait(0.0001) # wait 0.005 seconds before closing the trigger. This can be adapted to match the settings in BIOPAC that determine what the minimum amount of time a trigger must be open for inorder for it to be recognised as a digital stim event
ser.write('00'.encode('utf-8')) # Turn off all BIOPAC channels when you want to close all channels 

# If you wanted to send a trigger when a particular stimulus is first displayed in Psychopy:
# In the 'Begin' routine' tab
stimulus_pulse_started = False
stimulus_pulse_ended = False

# In the 'Each Frame' tab   
if stimulus.status == STARTED and not stimulus_pulse_started: #Change 'stimulus' to match the name of the component that you want to send the trigger for
    win.callOnFlip(ser.write, str.encode('03'))
    stimulus_pulse_start_time = globalClock.getTime()
    stimulus_pulse_started  = True

if stimulus_pulse_started and not stimulus_pulse_ended:
    if globalClock.getTime() - stimulus_pulse_start_time >= 0.005:
        win.callOnFlip(ser.write, str.encode('00'))
        stimulus_pulse_ended = True    

#In the 'End Routine' tab
ser.write ('RR'.encode('utf-8'))

#at the end of your code make sure you close the port
ser.close