#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on January 22, 2024, at 09:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_prac
import pandas as pd
import random

#prefs.hardware['audioLib'] = ['ptb','pygame','pyo']

#stim set
chars = ['X','R','T','J','L','P','N','F','B',0,1,2,3,4,5,6,7,8,9]

###SETUP BIOPAC SERIAL CONNECTION###
import serial
ser = serial.Serial("COM4",115200, timeout=1, bytesize=8, stopbits=1) # This must always be used before sending any triggers, it specifies the settings for the serial port.Exact settings should be customised to your specific port 
ser.open # Open the port
ser.write('RR'.encode()) # Reset the port so that its ready for the first trigger
#####################

# TEST HEX CODES HERE #
#ser.write('80'.encode()) # channel 28
#core.wait(0.5)
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'misophonia_max'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\lab\\Documents\\AttentionPhysiology\\Task\\mis v5\\misophonia_max_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.WARNING)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 720], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, experiment_code='misophonia_max', session_code=ioSession, datastore_name=thisExp.dataFileName, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions" ---
    intro_text = visual.TextStim(win=win, name='intro_text',
        text="Instructions\n\nIn this experiment, a string of 9 numbers and letters will be diplayed on the screen in a grid. For each number or letter in the string, you must indicate if it is a number or a letter by pressing the 'N' or 'L' keys.\n\nFor example, if the following is displayed on the screen:\n\nX4F\nBR4\n6S7\n\nA correct reponse wouild be to press the following sequence of keys on your keyboard: 'L, N, L, L, L, N, N, L, N', one keypress for each letter shown in order.\n\nAs you perform the task, we will play different sounds in the background.\n\nWe will begin with some practice trials with feedback.\n\nPlease press the spacebar to continue.",
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    intro_key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "practice" ---
    # Run 'Begin Experiment' code from code_prac
    timer = core.CountdownTimer(0) # init timer at 0
    current_sound = {}
    sound_currently_playing = 0
    sound_played_this_trial = 0
    n_prac = 5
    break_switch = 0
    
    # Load the sound file paths from the CSV file
    sound_df = pd.read_csv("sound_key.csv")#[0:2] #LESS TRIALS FOR TESTING
    sound_dict = sound_df.to_dict('records')
    sound_dict = sound_dict + sound_dict
    no_sound = [{}] * len(sound_dict) #append 50% empty trials
    for e in no_sound:
        sound_dict.append(e)
    random.shuffle(sound_dict) # Shuffle the list of sound file paths so that each sound is randomly ordered
    stim_prac = visual.TextStim(win=win, name='stim_prac',
        text='',
        font='Monaco',
        pos=(0, -.1), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    feedback = visual.TextStim(win=win, name='feedback',
        text='',
        font='Open Sans',
        pos=(0, -.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_prac = keyboard.Keyboard()
    fix_prac = visual.TextStim(win=win, name='fix_prac',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "end_prac" ---
    end_prac_text = visual.TextStim(win=win, name='end_prac_text',
        text='The practice trails have ended and we will now start the main task. It will take around 25 minutes.\n\nPlease press the spacebar to continue.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    end_prac_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "trial" ---
    stim = visual.TextStim(win=win, name='stim',
        text='',
        font='monaco',
        pos=(0, -.1), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard()
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "break_screen" ---
    break_text = visual.TextStim(win=win, name='break_text',
        text='This is the half-way point of the trials.\n\nTake a break and press the Spacebar when you are ready to continue.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    break_key = keyboard.Keyboard()
    
    # --- Initialize components for Routine "fin" ---
    text = visual.TextStim(win=win, name='text',
        text='END\n\nThank you for taking part in this experiment',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions.started', globalClock.getTime())
    intro_key_resp.keys = []
    intro_key_resp.rt = []
    _intro_key_resp_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [intro_text, intro_key_resp]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_text* updates
        
        # if intro_text is starting this frame...
        if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_text.frameNStart = frameN  # exact frame index
            intro_text.tStart = t  # local t and not account for scr refresh
            intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_text.started')
            # update status
            intro_text.status = STARTED
            intro_text.setAutoDraw(True)
        
        # if intro_text is active this frame...
        if intro_text.status == STARTED:
            # update params
            pass
        
        # *intro_key_resp* updates
        waitOnFlip = False
        
        # if intro_key_resp is starting this frame...
        if intro_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_key_resp.frameNStart = frameN  # exact frame index
            intro_key_resp.tStart = t  # local t and not account for scr refresh
            intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_key_resp.started')
            # update status
            intro_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(intro_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if intro_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = intro_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro_key_resp_allKeys.extend(theseKeys)
            if len(_intro_key_resp_allKeys):
                intro_key_resp.keys = _intro_key_resp_allKeys[-1].name  # just the last key pressed
                intro_key_resp.rt = _intro_key_resp_allKeys[-1].rt
                intro_key_resp.duration = _intro_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions.stopped', globalClock.getTime())
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_loop = data.TrialHandler(nReps=n_prac, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='prac_loop')
    thisExp.addLoop(prac_loop)  # add the loop to the experiment
    thisPrac_loop = prac_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_loop.rgb)
    if thisPrac_loop != None:
        for paramName in thisPrac_loop:
            globals()[paramName] = thisPrac_loop[paramName]
    
    for thisPrac_loop in prac_loop:
        currentLoop = prac_loop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_loop.rgb)
        if thisPrac_loop != None:
            for paramName in thisPrac_loop:
                globals()[paramName] = thisPrac_loop[paramName]
        
        # --- Prepare to start Routine "practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practice.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_prac
        # Trigger for 'begin practice trials
        if prac_loop.thisN == 0:
            ser.write('01'.encode()) # channel 20
            core.wait(0.0001)
            ser.write('00'.encode())
        
        #make stim
        random.shuffle(chars)
        chars_tr = chars[0:9]
        
        #display stim
        chars_disp = ''
        for i, c in enumerate(chars_tr):
            if (i+1) % 3 > 0:
                add_char = '   '
            else:
                add_char = '\n\n'
            chars_disp += str(c) + add_char
        
        #check if sound currently playing
        if sound_currently_playing == 0:
            sound_played_this_trial = 0
            print('SOUND NOT PLAYING AT TRIAL START')
            key_start = random.randint(2, 5)
        else:
            print('SOUND PLAYING AT TRIAL START')
        
        #feedback
        fdbk = ''
        toggle = 0
        
        #sound option 2
        #try:
        #    clip
        #except NameError:
        #    print('no clip yet')
        #else:
        #    print(clip.status)
        #    print(clip._checkPlaybackFinished())
        stim_prac.setText(chars_disp)
        key_prac.keys = []
        key_prac.rt = []
        _key_prac_allKeys = []
        # keep track of which components have finished
        practiceComponents = [stim_prac, feedback, key_prac, fix_prac]
        for thisComponent in practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_prac
            #make double sure only the first 9 presses are being captured: https://discourse.psychopy.org/t/end-routine-after-two-key-presses/2132/6
            if len(key_prac.keys) > 9:
                key_prac.keys = key_prac.keys[0:9]
                
            #if sound not playing when routine began, and timer is done, and correct number of key presses
            if len(key_prac.keys) == key_start and sound_currently_playing == 0 and sound_played_this_trial == 0: 
                current_sound = sound_dict[random.randint(0,len(sound_dict)-1)]
                sound_currently_playing = 1
                sound_played_this_trial = 1
                if current_sound == {}:
                    timer = core.CountdownTimer(0)
                    ser.write('10'.encode()) # Turn on BIOPAC channel 24
                else:
                    clip = sound.Sound(current_sound['filepath'], stereo=True)
                    clip.play()
                    ###BIOPAC TRIGGERS####
                    if current_sound['condition'] == 'misophonic':
                        ser.write('02'.encode()) # Turn on BIOPAC channel 21
                    elif current_sound['condition'] == 'neutral':
                        ser.write('04'.encode()) # Turn on BIOPAC channel 22
                    elif current_sound['condition'] == 'unpleasant':
                        ser.write('08'.encode()) # Turn on BIOPAC channel 23
                    #######################
                    timer = core.CountdownTimer(clip.getDuration())
            
            # Trigger for when sound stops playing
            if timer.getTime() <= 0 and sound_currently_playing == 1 and current_sound != {}: #if audio trial, when timer runs out
                sound_currently_playing = 0
                ser.write('00'.encode())
            
            #check if keypress is correct
            if len(key_prac.keys) == 0:
                fdbk = ''
            elif (key_prac.keys[-1] == 'n' and type(chars[len(key_prac.keys)-1]) == int) or (key_prac.keys[-1] == 'l' and type(chars[len(key_prac.keys)-1]) == str):
                fdbk = 'Correct'
            else:
                fdbk = 'Incorrect'
            
            # if total number of key presses reached, display last press for a frame and move on 
            # or: https://psychopy.org/_modules/psychopy/session.html
            if len(key_prac.keys) == 9:
                if toggle == 0: #needs an extra frame to render feedback on last button press
                    toggle = 1
                else:
                    core.wait(.5) #show feedback for half a second
                    continueRoutine = False #end routine
            
            # *stim_prac* updates
            
            # if stim_prac is starting this frame...
            if stim_prac.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                stim_prac.frameNStart = frameN  # exact frame index
                stim_prac.tStart = t  # local t and not account for scr refresh
                stim_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_prac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_prac.started')
                # update status
                stim_prac.status = STARTED
                stim_prac.setAutoDraw(True)
            
            # if stim_prac is active this frame...
            if stim_prac.status == STARTED:
                # update params
                pass
            
            # *feedback* updates
            
            # if feedback is starting this frame...
            if feedback.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                feedback.frameNStart = frameN  # exact frame index
                feedback.tStart = t  # local t and not account for scr refresh
                feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback.started')
                # update status
                feedback.status = STARTED
                feedback.setAutoDraw(True)
            
            # if feedback is active this frame...
            if feedback.status == STARTED:
                # update params
                feedback.setText(fdbk, log=False)
            
            # *key_prac* updates
            waitOnFlip = False
            
            # if key_prac is starting this frame...
            if key_prac.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_prac.frameNStart = frameN  # exact frame index
                key_prac.tStart = t  # local t and not account for scr refresh
                key_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_prac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_prac.started')
                # update status
                key_prac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_prac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_prac.status == STARTED and not waitOnFlip:
                theseKeys = key_prac.getKeys(keyList=['l','n'], ignoreKeys=["escape"], waitRelease=False)
                _key_prac_allKeys.extend(theseKeys)
                if len(_key_prac_allKeys):
                    key_prac.keys = [key.name for key in _key_prac_allKeys]  # storing all keys
                    key_prac.rt = [key.rt for key in _key_prac_allKeys]
                    key_prac.duration = [key.duration for key in _key_prac_allKeys]
                    # was this correct?
                    if (key_prac.keys == str('')) or (key_prac.keys == ''):
                        key_prac.corr = 1
                    else:
                        key_prac.corr = 0
            
            # *fix_prac* updates
            
            # if fix_prac is starting this frame...
            if fix_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_prac.frameNStart = frameN  # exact frame index
                fix_prac.tStart = t  # local t and not account for scr refresh
                fix_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_prac, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_prac.started')
                # update status
                fix_prac.status = STARTED
                fix_prac.setAutoDraw(True)
            
            # if fix_prac is active this frame...
            if fix_prac.status == STARTED:
                # update params
                pass
            
            # if fix_prac is stopping this frame...
            if fix_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_prac.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_prac.tStop = t  # not accounting for scr refresh
                    fix_prac.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_prac.stopped')
                    # update status
                    fix_prac.status = FINISHED
                    fix_prac.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice" ---
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practice.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_prac
        if current_sound == {}:
            sound_currently_playing = 0
            ser.write('00'.encode())
        
        # end practice loop
        if prac_loop.thisN+1 == n_prac:
            if timer.getTime() > 0: #stop any sound being played
                clip.stop()
                timer = core.CountdownTimer(0)
            sound_currently_playing = 0
            sound_played_this_trial = 0
            ser.write('00'.encode()) #reset trigger signal
        # check responses
        if key_prac.keys in ['', [], None]:  # No response was made
            key_prac.keys = None
            # was no response the correct answer?!
            if str('').lower() == 'none':
               key_prac.corr = 1;  # correct non-response
            else:
               key_prac.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_loop (TrialHandler)
        prac_loop.addData('key_prac.keys',key_prac.keys)
        prac_loop.addData('key_prac.corr', key_prac.corr)
        if key_prac.keys != None:  # we had a response
            prac_loop.addData('key_prac.rt', key_prac.rt)
            prac_loop.addData('key_prac.duration', key_prac.duration)
        # the Routine "practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed n_prac repeats of 'prac_loop'
    
    
    # --- Prepare to start Routine "end_prac" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end_prac.started', globalClock.getTime())
    end_prac_resp.keys = []
    end_prac_resp.rt = []
    _end_prac_resp_allKeys = []
    # keep track of which components have finished
    end_pracComponents = [end_prac_text, end_prac_resp]
    for thisComponent in end_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_prac" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_prac_text* updates
        
        # if end_prac_text is starting this frame...
        if end_prac_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_prac_text.frameNStart = frameN  # exact frame index
            end_prac_text.tStart = t  # local t and not account for scr refresh
            end_prac_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_prac_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_prac_text.started')
            # update status
            end_prac_text.status = STARTED
            end_prac_text.setAutoDraw(True)
        
        # if end_prac_text is active this frame...
        if end_prac_text.status == STARTED:
            # update params
            pass
        
        # *end_prac_resp* updates
        waitOnFlip = False
        
        # if end_prac_resp is starting this frame...
        if end_prac_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_prac_resp.frameNStart = frameN  # exact frame index
            end_prac_resp.tStart = t  # local t and not account for scr refresh
            end_prac_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_prac_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_prac_resp.started')
            # update status
            end_prac_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_prac_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_prac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_prac_resp.status == STARTED and not waitOnFlip:
            theseKeys = end_prac_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _end_prac_resp_allKeys.extend(theseKeys)
            if len(_end_prac_resp_allKeys):
                end_prac_resp.keys = _end_prac_resp_allKeys[-1].name  # just the last key pressed
                end_prac_resp.rt = _end_prac_resp_allKeys[-1].rt
                end_prac_resp.duration = _end_prac_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_prac" ---
    for thisComponent in end_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end_prac.stopped', globalClock.getTime())
    # the Routine "end_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1000.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from code
        # Trigger for 'begin experimental trials'
        if trials.thisN == 0:
            ser.write('01'.encode())
            core.wait(0.0001)
            ser.write('00'.encode())
        
        #make stim
        random.shuffle(chars)
        chars_tr = chars[0:9]
        thisExp.addData('stim',chars_tr)
        
        #display stim
        chars_disp = ''
        for i, c in enumerate(chars_tr):
            if (i+1) % 3 > 0:
                add_char = '   '
            else:
                add_char = '\n\n'
            chars_disp += str(c) + add_char
        
        #get key press number to start sound on
        if sound_currently_playing == 0:
            print('SOUND NOT PLAYING AT TRIAL START')
            sound_played_this_trial = 0
            key_start = random.randint(2, 5)
            thisExp.addData('key_start',key_start)
        else:
            print('SOUND PLAYING AT TRIAL START')
            thisExp.addData('sound','previous_trial')
        
        # if restarting after the break
        if break_switch == 1: #sound_df is original dataset, 1/4 the amount of trials
            break_switch = 0
            ser.write('01'.encode()) # blip for break end
            core.wait(0.0001)
            ser.write('00'.encode())
        stim.setText(chars_disp)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [stim, key_resp, fix]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            #make double sure only the first 9 presses are being captured: https://discourse.psychopy.org/t/end-routine-after-two-key-presses/2132/6
            if len(key_resp.keys) > 9:
                key_resp.keys = key_resp.keys[0:9]
            
            #if sound not playing when routine began, and correct number of key presses
            if len(key_resp.keys) == key_start and sound_currently_playing == 0 and sound_played_this_trial == 0: 
                current_sound = sound_dict.pop()
                sound_currently_playing = 1
                sound_played_this_trial = 1
                if current_sound == {}:
                    timer = core.CountdownTimer(0)
                    ser.write('10'.encode()) # Turn on BIOPAC channel 24
                    # Add data
                    thisExp.addData('sound','silent_trial')
                else:
                    clip = sound.Sound(current_sound['filepath'], stereo=True)
                    clip.play()
                    ###BIOPAC TRIGGERS####
                    if current_sound['condition'] == 'misophonic':
                        ser.write('02'.encode()) # Turn on BIOPAC channel 21
                    elif current_sound['condition'] == 'neutral':
                        ser.write('04'.encode()) # Turn on BIOPAC channel 22
                    elif current_sound['condition'] == 'unpleasant':
                        ser.write('08'.encode()) # Turn on BIOPAC channel 23
                    #######################
                    timer = core.CountdownTimer(clip.getDuration())
                    # Add data
                    thisExp.addData('sound',current_sound['filepath'])
                    thisExp.addData('condition',current_sound['condition'])
                    thisExp.addData('sound_started',core.getTime())
                    thisExp.addData('sound_duration',clip.duration)
                    thisExp.addData('sound_end',core.getTime()+clip.duration)
            
            if timer.getTime() <= 0 and sound_currently_playing == 1 and current_sound != {}: #if audio trial, when timer runs out
                ser.write('00'.encode())
                sound_currently_playing = 0
            
            # if 9th key press either next trial or end exp
            if len(key_resp.keys) == 9:
                if len(sound_dict) == 0 and timer.getTime() <= 0:
                    trials.finished = True
                    # Trigger for 'end experimental trials'
                    ser.write('01'.encode())
                    core.wait(0.0001)
                    ser.write('00'.encode())
                continueRoutine = False
            
            # *stim* updates
            
            # if stim is starting this frame...
            if stim.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                stim.frameNStart = frameN  # exact frame index
                stim.tStart = t  # local t and not account for scr refresh
                stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim.started')
                # update status
                stim.status = STARTED
                stim.setAutoDraw(True)
            
            # if stim is active this frame...
            if stim.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['l','n'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                    key_resp.rt = [key.rt for key in _key_resp_allKeys]
                    key_resp.duration = [key.duration for key in _key_resp_allKeys]
                    # was this correct?
                    if (key_resp.keys == str('')) or (key_resp.keys == ''):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
            
            # *fix* updates
            
            # if fix is starting this frame...
            if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix.started')
                # update status
                fix.status = STARTED
                fix.setAutoDraw(True)
            
            # if fix is active this frame...
            if fix.status == STARTED:
                # update params
                pass
            
            # if fix is stopping this frame...
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.stopped')
                    # update status
                    fix.status = FINISHED
                    fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # Run 'End Routine' code from code
        if current_sound == {}:
            sound_currently_playing = 0
            ser.write('00'.encode())
        
        # store accuracy
        correct = []
        for i, c in enumerate(chars[0:9]):
            if (str(c).isnumeric() and key_resp.keys[i]=='n') or (str(c).isnumeric()==False and key_resp.keys[i]=='l'):
                key_resp.corr += 1
                correct.append(True)
            else:
                correct.append(False)
        thisExp.addData("correct_trials", correct)
        
        # Present break screen
        if len(sound_dict) == len(sound_df)*2 and sound_currently_playing == 0: #sound_df is original dataset, 1/4 the amount of trials
            break_switch = 1
            ser.write('01'.encode()) # blip for break start
            core.wait(0.0001)
            ser.write('00'.encode())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str('').lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        break_loop = data.TrialHandler(nReps=break_switch, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='break_loop')
        thisExp.addLoop(break_loop)  # add the loop to the experiment
        thisBreak_loop = break_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBreak_loop.rgb)
        if thisBreak_loop != None:
            for paramName in thisBreak_loop:
                globals()[paramName] = thisBreak_loop[paramName]
        
        for thisBreak_loop in break_loop:
            currentLoop = break_loop
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisBreak_loop.rgb)
            if thisBreak_loop != None:
                for paramName in thisBreak_loop:
                    globals()[paramName] = thisBreak_loop[paramName]
            
            # --- Prepare to start Routine "break_screen" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('break_screen.started', globalClock.getTime())
            break_key.keys = []
            break_key.rt = []
            _break_key_allKeys = []
            # keep track of which components have finished
            break_screenComponents = [break_text, break_key]
            for thisComponent in break_screenComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "break_screen" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *break_text* updates
                
                # if break_text is starting this frame...
                if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    break_text.frameNStart = frameN  # exact frame index
                    break_text.tStart = t  # local t and not account for scr refresh
                    break_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'break_text.started')
                    # update status
                    break_text.status = STARTED
                    break_text.setAutoDraw(True)
                
                # if break_text is active this frame...
                if break_text.status == STARTED:
                    # update params
                    pass
                
                # *break_key* updates
                waitOnFlip = False
                
                # if break_key is starting this frame...
                if break_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    break_key.frameNStart = frameN  # exact frame index
                    break_key.tStart = t  # local t and not account for scr refresh
                    break_key.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(break_key, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'break_key.started')
                    # update status
                    break_key.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(break_key.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if break_key.status == STARTED and not waitOnFlip:
                    theseKeys = break_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _break_key_allKeys.extend(theseKeys)
                    if len(_break_key_allKeys):
                        break_key.keys = _break_key_allKeys[-1].name  # just the last key pressed
                        break_key.rt = _break_key_allKeys[-1].rt
                        break_key.duration = _break_key_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in break_screenComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "break_screen" ---
            for thisComponent in break_screenComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('break_screen.stopped', globalClock.getTime())
            # check responses
            if break_key.keys in ['', [], None]:  # No response was made
                break_key.keys = None
            break_loop.addData('break_key.keys',break_key.keys)
            if break_key.keys != None:  # we had a response
                break_loop.addData('break_key.rt', break_key.rt)
                break_loop.addData('break_key.duration', break_key.duration)
            # the Routine "break_screen" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed break_switch repeats of 'break_loop'
        
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1000.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "fin" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('fin.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    finComponents = [text, key_resp_2]
    for thisComponent in finComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fin" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fin" ---
    for thisComponent in finComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('fin.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "fin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # Run 'End Experiment' code from code_prac
    ser.write('RR'.encode()) #reset trigger signal
    ser.close
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
