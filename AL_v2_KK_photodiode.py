#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Tue Dec  4 12:09:09 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# module import for labjack 
import time 

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'AL'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'block': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expName, expInfo['date'], expInfo['participant'], expInfo['block'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color= 'white', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Start_ready0"
Start_ready0Clock = core.Clock()
start_msg = visual.TextStim(win=win, name='start_msg',
    text='Experiment will start in a moment. \n\nPreferred hand for responding? (l / r)',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=5, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_ready1"
Start_ready1Clock = core.Clock()
ready_1 = visual.TextStim(win=win, name='ready_1',
    text="Please press '1'.",
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_ready2"
Start_ready2Clock = core.Clock()
ready_2 = visual.TextStim(win=win, name='ready_2',
    text="Please press '2'.",
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_ready3"
Start_ready3Clock = core.Clock()
ready_3 = visual.TextStim(win=win, name='ready_3',
    text="Please press '3'.",
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "prestim_fix"
prestim_fixClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "show_obj"
show_objClock = core.Clock()
stim = visual.ImageStim(
    win=win, name='stim',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# add trigger to show_obj 
trigger_square = visual.Rect(
    win=win, name='polygon',units='cm', 
    width=(3,3)[0], height=(3,3)[1],
    ori=0, pos=(-23.2, -14), 
    lineWidth=1, lineColor=u'black', lineColorSpace='rgb',
    fillColor=u'black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "delay"
delayClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "get_response"
get_responseClock = core.Clock()
showchoice_1 = visual.TextStim(win=win, name='showchoice_1',
    text='default text',
    font=u'Arial',
    pos=(-0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color=u'grey', colorSpace='rgb', opacity=1,
    depth=-1.0);
showchoice_2 = visual.TextStim(win=win, name='showchoice_2',
    text=u'2',
    font=u'Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=u'grey', colorSpace='rgb', opacity=1,
    depth=-2.0);
showchoise_3 = visual.TextStim(win=win, name='showchoise_3',
    text=u'3',
    font=u'Arial',
    pos=(0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color=u'grey', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "showresponse"
showresponseClock = core.Clock()
tshowresponse = 0
showresponse_1_1 = visual.TextStim(win=win, name='showresponse_1_1',
    text='1',
    font='Arial',
    pos=(-0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color='RoyalBlue', colorSpace='rgb', opacity=1,
    depth=-1.0);
showresponse_1_2 = visual.TextStim(win=win, name='showresponse_1_2',
    text='1',
    font='Arial',
    pos=(-0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-2.0);
showresponse_1_3 = visual.TextStim(win=win, name='showresponse_1_3',
    text='1',
    font='Arial',
    pos=(-0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-3.0);
showresponse_2_1 = visual.TextStim(win=win, name='showresponse_2_1',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-4.0);
showresponse_2_2 = visual.TextStim(win=win, name='showresponse_2_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='RoyalBlue', colorSpace='rgb', opacity=1,
    depth=-5.0);
showresponse_2_3 = visual.TextStim(win=win, name='showresponse_2_3',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-6.0);
showresponse_3_1 = visual.TextStim(win=win, name='showresponse_3_1',
    text='3',
    font='Arial',
    pos=(0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-7.0);
showresponse_3_2 = visual.TextStim(win=win, name='showresponse_3_2',
    text='3',
    font='Arial',
    pos=(0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=-8.0);
showresponse_3_3 = visual.TextStim(win=win, name='showresponse_3_3',
    text='3',
    font='Arial',
    pos=(0.45, 0), height=0.15, wrapWidth=None, ori=0, 
    color='RoyalBlue', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "show_feedback"
show_feedbackClock = core.Clock()
fbmsg = 'foo!'
fbcol = 'grey'; 
feedback_msg = visual.TextStim(win=win, name='feedback_msg',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "exit_msg"
exit_msgClock = core.Clock()
exit = visual.TextStim(win=win, name='exit',
    text='You have completed this block. \n\nThank you!! \n\nPress space bar to exit. ',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=5, ori=0, 
    color='grey', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start_ready0"-------
t = 0
Start_ready0Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_start_1 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_ready0Components = [start_msg, key_start_1]
for thisComponent in Start_ready0Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_ready0"-------
while continueRoutine:
    # get current time
    t = Start_ready0Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_msg* updates
    if t >= 0.0 and start_msg.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_msg.tStart = t
        start_msg.frameNStart = frameN  # exact frame index
        start_msg.setAutoDraw(True)
    
    # *key_start_1* updates
    if t >= 0.0 and key_start_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_start_1.tStart = t
        key_start_1.frameNStart = frameN  # exact frame index
        key_start_1.status = STARTED
        # keyboard checking is just starting
        key_start_1.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_start_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['l', 'r'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_start_1.keys = theseKeys[-1]  # just the last key pressed
            key_start_1.rt = key_start_1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_ready0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_ready0"-------
for thisComponent in Start_ready0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_start_1.keys in ['', [], None]:  # No response was made
    key_start_1.keys=None
thisExp.addData('key_start_1.keys',key_start_1.keys)
if key_start_1.keys != None:  # we had a response
    thisExp.addData('key_start_1.rt', key_start_1.rt)
thisExp.nextEntry()
# the Routine "Start_ready0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
#
#send_pulse_dac0()
#time.sleep(0.5)
#send_pulse_dac0()
#time.sleep(0.5)
#send_pulse_dac0()
#time.sleep(0.5)

# ------Prepare to start Routine "Start_ready1"-------
t = 0
Start_ready1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_1r = event.BuilderKeyResponse()
key_resp_1l = event.BuilderKeyResponse()
# keep track of which components have finished
Start_ready1Components = [ready_1, key_resp_1r, key_resp_1l]
for thisComponent in Start_ready1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_ready1"-------
while continueRoutine:
    # get current time
    t = Start_ready1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_1* updates
    if t >= 0.0 and ready_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_1.tStart = t
        ready_1.frameNStart = frameN  # exact frame index
        ready_1.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ready_1.status == STARTED and t >= frameRemains:
        ready_1.setAutoDraw(False)
    
    # *key_resp_1r* updates
    if (key_start_1.keys == "r") and key_resp_1r.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_1r.tStart = t
        key_resp_1r.frameNStart = frameN  # exact frame index
        key_resp_1r.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_1r.status == STARTED:
        theseKeys = event.getKeys(keyList=['comma'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *key_resp_1l* updates
    if (key_start_1.keys == "l") and key_resp_1l.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_1l.tStart = t
        key_resp_1l.frameNStart = frameN  # exact frame index
        key_resp_1l.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_1l.status == STARTED:
        theseKeys = event.getKeys(keyList=['z'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_ready1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_ready1"-------
for thisComponent in Start_ready1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start_ready1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_ready2"-------
t = 0
Start_ready2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2r = event.BuilderKeyResponse()
key_resp_2l = event.BuilderKeyResponse()
# keep track of which components have finished
Start_ready2Components = [ready_2, key_resp_2r, key_resp_2l]
for thisComponent in Start_ready2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_ready2"-------
while continueRoutine:
    # get current time
    t = Start_ready2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_2* updates
    if t >= 0.0 and ready_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_2.tStart = t
        ready_2.frameNStart = frameN  # exact frame index
        ready_2.setAutoDraw(True)
    if ready_2.status == STARTED and bool(key_resp_2r.keys or key_resp_2l.keys):
        ready_2.setAutoDraw(False)
    
    # *key_resp_2r* updates
    if (key_start_1.keys == 'r') and key_resp_2r.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2r.tStart = t
        key_resp_2r.frameNStart = frameN  # exact frame index
        key_resp_2r.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2r.status == STARTED:
        theseKeys = event.getKeys(keyList=['period'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *key_resp_2l* updates
    if (key_start_1.keys == 'l') and key_resp_2l.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2l.tStart = t
        key_resp_2l.frameNStart = frameN  # exact frame index
        key_resp_2l.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2l.status == STARTED:
        theseKeys = event.getKeys(keyList=['x'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_ready2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_ready2"-------
for thisComponent in Start_ready2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start_ready2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_ready3"-------
t = 0
Start_ready3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3r = event.BuilderKeyResponse()
key_resp_3l = event.BuilderKeyResponse()
# keep track of which components have finished
Start_ready3Components = [ready_3, key_resp_3r, key_resp_3l]
for thisComponent in Start_ready3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_ready3"-------
while continueRoutine:
    # get current time
    t = Start_ready3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ready_3* updates
    if t >= 0.0 and ready_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_3.tStart = t
        ready_3.frameNStart = frameN  # exact frame index
        ready_3.setAutoDraw(True)
    if ready_3.status == STARTED and bool(key_resp_3r.keys or key_resp_3l.keys):
        ready_3.setAutoDraw(False)
    
    # *key_resp_3r* updates
    if (key_start_1.keys == 'r') and key_resp_3r.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3r.tStart = t
        key_resp_3r.frameNStart = frameN  # exact frame index
        key_resp_3r.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3r.status == STARTED:
        theseKeys = event.getKeys(keyList=['slash'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *key_resp_3l* updates
    if (key_start_1.keys == 'l') and key_resp_3l.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3l.tStart = t
        key_resp_3l.frameNStart = frameN  # exact frame index
        key_resp_3l.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3l.status == STARTED:
        theseKeys = event.getKeys(keyList=['c'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_ready3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_ready3"-------
for thisComponent in Start_ready3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start_ready3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('config_files_v2/AL_config_'+expInfo['participant']+'_'+expInfo['block']+'.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "prestim_fix"-------
    t = 0
    prestim_fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    prestim_fixComponents = [text]
    for thisComponent in prestim_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "prestim_fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prestim_fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prestim_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prestim_fix"-------
    for thisComponent in prestim_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "show_obj"-------
    t = 0
    show_objClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    stim.setImage(stim_obj)
    
    # keep track of which components have finished
    show_objComponents = [stim, trigger_square]
    for thisComponent in show_objComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "show_obj"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = show_objClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trigger_square* updates
#        if t >= 0 and trigger_square.status == NOT_STARTED: 
#            # keep track of start time/frame for later
#            trigger_square.tStart = t
#            trigger_square.frameNStart = frameN  # exact frame index
#            trigger_square.setAutoDraw(True)
#        frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
#        if trigger_square.status == STARTED and t >= frameRemains:
#            trigger_square.setAutoDraw(False)
            
        # *stim* updates
        if t >= 0 and stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim.tStart = t
            stim.frameNStart = frameN  # exact frame index
            stim.setAutoDraw(True)
            trigger_square.setAutoDraw(True)
        frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stim.status == STARTED and t >= frameRemains:
            stim.setAutoDraw(False)
            trigger_square.setAutoDraw(False)    
            
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_objComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "show_obj"-------
    for thisComponent in show_objComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "delay"-------
    t = 0
    delayClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    delayComponents = [blank]
    for thisComponent in delayComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "delay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = delayClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if t >= 0.0 and blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank.tStart = t
            blank.frameNStart = frameN  # exact frame index
            blank.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank.status == STARTED and t >= frameRemains:
            blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "delay"-------
    for thisComponent in delayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "get_response"-------
    t = 0
    get_responseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.500000) ##KK
    # update component parameters for each repeat
    get_resp = event.BuilderKeyResponse()
    showchoice_1.setText(u'1')
    # keep track of which components have finished
    get_responseComponents = [get_resp, showchoice_1, showchoice_2, showchoise_3]
    for thisComponent in get_responseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "get_response"-------
    while continueRoutine and routineTimer.getTime() > 0: ##KK
        # get current time
        t = get_responseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *get_resp* updates
        if t >= 0.0 and get_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            get_resp.tStart = t
            get_resp.frameNStart = frameN  # exact frame index
            get_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(get_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2.5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if get_resp.status == STARTED and t >= frameRemains:
            get_resp.status = STOPPED
        if get_resp.status == STARTED and key_start_1.keys == 'l': ## KK
            theseKeys = event.getKeys(keyList=['z', 'x', 'c'])## KK
            if len(theseKeys) > 0:  # at least one key was pressed
                get_resp.keys = theseKeys[-1]  # just the last key pressed
                get_resp.rt = get_resp.clock.getTime()
                # was this 'correct'?
                if (get_resp.keys == str(CorrectRespL)) or (get_resp.keys == CorrectRespL):## KK
                    get_resp.corr = 1
                else:
                    get_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        elif get_resp.status == STARTED and key_start_1.keys == 'r': ## KK            
            theseKeys = event.getKeys(keyList=['comma', 'period', 'slash'])## KK
            if len(theseKeys) > 0:  # at least one key was pressed
                get_resp.keys = theseKeys[-1]  # just the last key pressed
                get_resp.rt = get_resp.clock.getTime()
                # was this 'correct'?
                if (get_resp.keys == str(CorrectRespR)) or (get_resp.keys == CorrectRespR):## KK
                    get_resp.corr = 1
                else:
                    get_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *showchoice_1* updates
        if t >= 0.0 and showchoice_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            showchoice_1.tStart = t
            showchoice_1.frameNStart = frameN  # exact frame index
            showchoice_1.setAutoDraw(True)
        if showchoice_1.status == STARTED and bool(get_resp.keys):
            showchoice_1.setAutoDraw(False)
        
        # *showchoice_2* updates
        if t >= 0.0 and showchoice_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            showchoice_2.tStart = t
            showchoice_2.frameNStart = frameN  # exact frame index
            showchoice_2.setAutoDraw(True)
        if showchoice_2.status == STARTED and bool(get_resp.keys):
            showchoice_2.setAutoDraw(False)
        
        # *showchoise_3* updates
        if t >= 0.0 and showchoise_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            showchoise_3.tStart = t
            showchoise_3.frameNStart = frameN  # exact frame index
            showchoise_3.setAutoDraw(True)
        if showchoise_3.status == STARTED and bool(get_resp.keys):
            showchoise_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in get_responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "get_response"-------
    for thisComponent in get_responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if get_resp.keys in ['', [], None]:  # No response was made
        get_resp.keys=None
        get_resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('get_resp.keys',get_resp.keys)
    trials.addData('get_resp.corr', get_resp.corr)
    if get_resp.keys != None:  # we had a response
        trials.addData('get_resp.rt', get_resp.rt)
    # the Routine "get_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "showresponse"-------
    t = 0
    showresponseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if get_resp.keys:
        tshowresponse = 3.0 - get_resp.rt
    else:
        continueRoutine = False ##KK skip if no response
    
    # keep track of which components have finished
    showresponseComponents = [showresponse_1_1, showresponse_1_2, showresponse_1_3, showresponse_2_1, showresponse_2_2, showresponse_2_3, showresponse_3_1, showresponse_3_2, showresponse_3_3]
    for thisComponent in showresponseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "showresponse"-------
    while continueRoutine:
        # get current time
        t = showresponseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame      
        
        # *showresponse_1_1* updates
        if (get_resp.keys == 'z' or get_resp.keys == 'comma') and showresponse_1_1.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_1_1.tStart = t
            showresponse_1_1.frameNStart = frameN  # exact frame index
            showresponse_1_1.setAutoDraw(True)
        if showresponse_1_1.status == STARTED and t >= (showresponse_1_1.tStart + tshowresponse):
            showresponse_1_1.setAutoDraw(False)
            continueRoutine = False  ##KK
            
        # *showresponse_1_2* updates
        if (get_resp.keys == 'x' or get_resp.keys == 'period') and showresponse_1_2.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_1_2.tStart = t
            showresponse_1_2.frameNStart = frameN  # exact frame index
            showresponse_1_2.setAutoDraw(True)
        if showresponse_1_2.status == STARTED and t >= (showresponse_1_2.tStart + tshowresponse):
            showresponse_1_2.setAutoDraw(False)
            continueRoutine = False  ##KK
            
        # *showresponse_1_3* updates
        if (get_resp.keys == 'c' or get_resp.keys == 'slash' )  and showresponse_1_3.status == NOT_STARTED:  ##KK
            # keep track of start time/frame for later
            showresponse_1_3.tStart = t
            showresponse_1_3.frameNStart = frameN  # exact frame index
            showresponse_1_3.setAutoDraw(True)
        if showresponse_1_3.status == STARTED and t >= (showresponse_1_3.tStart + tshowresponse):
            showresponse_1_3.setAutoDraw(False)
            continueRoutine = False ##KK

        # *showresponse_2_1* updates
        if (get_resp.keys == 'z' or get_resp.keys == 'comma' ) and showresponse_2_1.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_2_1.tStart = t
            showresponse_2_1.frameNStart = frameN  # exact frame index
            showresponse_2_1.setAutoDraw(True)
        if showresponse_2_1.status == STARTED and t >= (showresponse_2_1.tStart + tshowresponse):
            showresponse_2_1.setAutoDraw(False)
            continueRoutine = False  ##KK
            
        # *showresponse_2_2* updates
        if (get_resp.keys == 'x' or get_resp.keys == 'period') and showresponse_2_2.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_2_2.tStart = t
            showresponse_2_2.frameNStart = frameN  # exact frame index
            showresponse_2_2.setAutoDraw(True)
        if showresponse_2_2.status == STARTED and t >= (showresponse_2_2.tStart + tshowresponse):
            showresponse_2_2.setAutoDraw(False)
            continueRoutine = False  ##KK
            
        # *showresponse_2_3* updates
        if (get_resp.keys == 'c' or get_resp.keys == 'slash') and showresponse_2_3.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_2_3.tStart = t
            showresponse_2_3.frameNStart = frameN  # exact frame index
            showresponse_2_3.setAutoDraw(True)
        if showresponse_2_3.status == STARTED and t >= (showresponse_2_3.tStart + tshowresponse):
            showresponse_2_3.setAutoDraw(False)
            continueRoutine = False  ##KK
            
        # *showresponse_3_1* updates
        if (get_resp.keys == 'z' or get_resp.keys == 'comma') and showresponse_3_1.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_3_1.tStart = t
            showresponse_3_1.frameNStart = frameN  # exact frame index
            showresponse_3_1.setAutoDraw(True)
        if showresponse_3_1.status == STARTED and t >= (showresponse_3_1.tStart + tshowresponse):
            showresponse_3_1.setAutoDraw(False)
            continueRoutine = False  ##KK
            
        # *showresponse_3_2* updates
        if (get_resp.keys == 'x' or get_resp.keys == 'period') and showresponse_3_2.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_3_2.tStart = t
            showresponse_3_2.frameNStart = frameN  # exact frame index
            showresponse_3_2.setAutoDraw(True)
        if showresponse_3_2.status == STARTED and t >= (showresponse_3_2.tStart + tshowresponse):
            showresponse_3_2.setAutoDraw(False)
            continueRoutine = False  ##KK
            
        # *showresponse_3_3* updates
        if (get_resp.keys == 'c' or get_resp.keys == 'slash') and showresponse_3_3.status == NOT_STARTED: ##KK
            # keep track of start time/frame for later
            showresponse_3_3.tStart = t
            showresponse_3_3.frameNStart = frameN  # exact frame index
            showresponse_3_3.setAutoDraw(True)
        if showresponse_3_3.status == STARTED and t >= (showresponse_3_3.tStart + tshowresponse):
            showresponse_3_3.setAutoDraw(False)
            continueRoutine = False ##KK
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in showresponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "showresponse"-------
    for thisComponent in showresponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "showresponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "show_feedback"-------
    t = 0
    show_feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    if not get_resp.keys:
        fbmsg = 'You did not respond!'
        fbcol = 'grey'; 
    elif get_resp.corr:
        fbmsg = 'correct!!'
        fbcol = 'LimeGreen'; 
    else: 
        fbmsg = 'incorrect'
        fbcol = 'OrangeRed'; 
    feedback_msg.setColor(fbcol, colorSpace='rgb')
    feedback_msg.setText(fbmsg)
    # keep track of which components have finished
    show_feedbackComponents = [feedback_msg]
    for thisComponent in show_feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "show_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = show_feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_msg* updates
        if t >= 0.1 and feedback_msg.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_msg.tStart = t
            feedback_msg.frameNStart = frameN  # exact frame index
            feedback_msg.setAutoDraw(True)
        frameRemains = 0.1 + 0.4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_msg.status == STARTED and t >= frameRemains:
            feedback_msg.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "show_feedback"-------
    for thisComponent in show_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "exit_msg"-------
t = 0
exit_msgClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
press_to_exit = event.BuilderKeyResponse()
# keep track of which components have finished
exit_msgComponents = [exit, press_to_exit]
for thisComponent in exit_msgComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "exit_msg"-------
while continueRoutine:
    # get current time
    t = exit_msgClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exit* updates
    if t >= 0.0 and exit.status == NOT_STARTED:
        # keep track of start time/frame for later
        exit.tStart = t
        exit.frameNStart = frameN  # exact frame index
        exit.setAutoDraw(True)
    
    # *press_to_exit* updates
    if t >= 0.0 and press_to_exit.status == NOT_STARTED:
        # keep track of start time/frame for later
        press_to_exit.tStart = t
        press_to_exit.frameNStart = frameN  # exact frame index
        press_to_exit.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if press_to_exit.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exit_msgComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exit_msg"-------
for thisComponent in exit_msgComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "exit_msg" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
