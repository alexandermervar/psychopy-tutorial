#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.0),
    on Mon Feb 22 00:19:37 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.0'
expName = 'libraryTutorialPsychoPy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mervar/OneDrive - Indiana University/COGS-Q 320/Projects/psychopy-tutorial/libraryTutorialPsychoPy_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome COGS-Q 320 Students!\n\nPsychoPy Tutorial with Alexander and Jenna',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEndWelcome = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StudyTrial"
StudyTrialClock = core.Clock()
keyStudyDemo = keyboard.Keyboard()
polygonStudy = visual.Polygon(
    win=win, name='polygonStudy',
    edges=100, size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "beginTest"
beginTestClock = core.Clock()
textBeginTest = visual.TextStim(win=win, name='textBeginTest',
    text='Press Space to Begin Test',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
spaceBeginTest = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "studyTest"
studyTestClock = core.Clock()
polygonTest = visual.Polygon(
    win=win, name='polygonTest',
    edges=100, size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "thankYou"
thankYouClock = core.Clock()
textThanks = visual.TextStim(win=win, name='textThanks',
    text='Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
keyEndWelcome.keys = []
keyEndWelcome.rt = []
_keyEndWelcome_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [textWelcome, keyEndWelcome]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keyEndWelcome* updates
    waitOnFlip = False
    if keyEndWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEndWelcome.frameNStart = frameN  # exact frame index
        keyEndWelcome.tStart = t  # local t and not account for scr refresh
        keyEndWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEndWelcome, 'tStartRefresh')  # time at next scr refresh
        keyEndWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEndWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEndWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEndWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyEndWelcome.getKeys(keyList=['space'], waitRelease=False)
        _keyEndWelcome_allKeys.extend(theseKeys)
        if len(_keyEndWelcome_allKeys):
            keyEndWelcome.keys = _keyEndWelcome_allKeys[-1].name  # just the last key pressed
            keyEndWelcome.rt = _keyEndWelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keyEndWelcome.keys in ['', [], None]:  # No response was made
    keyEndWelcome.keys = None
thisExp.addData('keyEndWelcome.keys',keyEndWelcome.keys)
if keyEndWelcome.keys != None:  # we had a response
    thisExp.addData('keyEndWelcome.rt', keyEndWelcome.rt)
thisExp.addData('keyEndWelcome.started', keyEndWelcome.tStartRefresh)
thisExp.addData('keyEndWelcome.stopped', keyEndWelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textBlank]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank500"-------
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBlank.started', textBlank.tStartRefresh)
thisExp.addData('textBlank.stopped', textBlank.tStopRefresh)

# set up handler to look after randomisation of conditions etc
studyLoops = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('studyItems.xlsm', selection='0:6'),
    seed=None, name='studyLoops')
thisExp.addLoop(studyLoops)  # add the loop to the experiment
thisStudyLoop = studyLoops.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudyLoop.rgb)
if thisStudyLoop != None:
    for paramName in thisStudyLoop:
        exec('{} = thisStudyLoop[paramName]'.format(paramName))

for thisStudyLoop in studyLoops:
    currentLoop = studyLoops
    # abbreviate parameter names if possible (e.g. rgb = thisStudyLoop.rgb)
    if thisStudyLoop != None:
        for paramName in thisStudyLoop:
            exec('{} = thisStudyLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "StudyTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    keyStudyDemo.keys = []
    keyStudyDemo.rt = []
    _keyStudyDemo_allKeys = []
    polygonStudy.setFillColor(shapeColor)
    # keep track of which components have finished
    StudyTrialComponents = [keyStudyDemo, polygonStudy]
    for thisComponent in StudyTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StudyTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StudyTrial"-------
    while continueRoutine:
        # get current time
        t = StudyTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StudyTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *keyStudyDemo* updates
        waitOnFlip = False
        if keyStudyDemo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyStudyDemo.frameNStart = frameN  # exact frame index
            keyStudyDemo.tStart = t  # local t and not account for scr refresh
            keyStudyDemo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyStudyDemo, 'tStartRefresh')  # time at next scr refresh
            keyStudyDemo.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyStudyDemo.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyStudyDemo.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyStudyDemo.status == STARTED and not waitOnFlip:
            theseKeys = keyStudyDemo.getKeys(keyList=['space'], waitRelease=False)
            _keyStudyDemo_allKeys.extend(theseKeys)
            if len(_keyStudyDemo_allKeys):
                keyStudyDemo.keys = _keyStudyDemo_allKeys[-1].name  # just the last key pressed
                keyStudyDemo.rt = _keyStudyDemo_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *polygonStudy* updates
        if polygonStudy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonStudy.frameNStart = frameN  # exact frame index
            polygonStudy.tStart = t  # local t and not account for scr refresh
            polygonStudy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonStudy, 'tStartRefresh')  # time at next scr refresh
            polygonStudy.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StudyTrial"-------
    for thisComponent in StudyTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyStudyDemo.keys in ['', [], None]:  # No response was made
        keyStudyDemo.keys = None
    studyLoops.addData('keyStudyDemo.keys',keyStudyDemo.keys)
    if keyStudyDemo.keys != None:  # we had a response
        studyLoops.addData('keyStudyDemo.rt', keyStudyDemo.rt)
    studyLoops.addData('keyStudyDemo.started', keyStudyDemo.tStartRefresh)
    studyLoops.addData('keyStudyDemo.stopped', keyStudyDemo.tStopRefresh)
    studyLoops.addData('polygonStudy.started', polygonStudy.tStartRefresh)
    studyLoops.addData('polygonStudy.stopped', polygonStudy.tStopRefresh)
    # the Routine "StudyTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [textBlank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(True)
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    studyLoops.addData('textBlank.started', textBlank.tStartRefresh)
    studyLoops.addData('textBlank.stopped', textBlank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'studyLoops'


# ------Prepare to start Routine "beginTest"-------
continueRoutine = True
# update component parameters for each repeat
spaceBeginTest.keys = []
spaceBeginTest.rt = []
_spaceBeginTest_allKeys = []
# keep track of which components have finished
beginTestComponents = [textBeginTest, spaceBeginTest]
for thisComponent in beginTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beginTest"-------
while continueRoutine:
    # get current time
    t = beginTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBeginTest* updates
    if textBeginTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBeginTest.frameNStart = frameN  # exact frame index
        textBeginTest.tStart = t  # local t and not account for scr refresh
        textBeginTest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBeginTest, 'tStartRefresh')  # time at next scr refresh
        textBeginTest.setAutoDraw(True)
    
    # *spaceBeginTest* updates
    waitOnFlip = False
    if spaceBeginTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spaceBeginTest.frameNStart = frameN  # exact frame index
        spaceBeginTest.tStart = t  # local t and not account for scr refresh
        spaceBeginTest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceBeginTest, 'tStartRefresh')  # time at next scr refresh
        spaceBeginTest.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(spaceBeginTest.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(spaceBeginTest.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if spaceBeginTest.status == STARTED and not waitOnFlip:
        theseKeys = spaceBeginTest.getKeys(keyList=['space'], waitRelease=False)
        _spaceBeginTest_allKeys.extend(theseKeys)
        if len(_spaceBeginTest_allKeys):
            spaceBeginTest.keys = _spaceBeginTest_allKeys[-1].name  # just the last key pressed
            spaceBeginTest.rt = _spaceBeginTest_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginTest"-------
for thisComponent in beginTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBeginTest.started', textBeginTest.tStartRefresh)
thisExp.addData('textBeginTest.stopped', textBeginTest.tStopRefresh)
# check responses
if spaceBeginTest.keys in ['', [], None]:  # No response was made
    spaceBeginTest.keys = None
thisExp.addData('spaceBeginTest.keys',spaceBeginTest.keys)
if spaceBeginTest.keys != None:  # we had a response
    thisExp.addData('spaceBeginTest.rt', spaceBeginTest.rt)
thisExp.addData('spaceBeginTest.started', spaceBeginTest.tStartRefresh)
thisExp.addData('spaceBeginTest.stopped', spaceBeginTest.tStopRefresh)
thisExp.nextEntry()
# the Routine "beginTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textBlank]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank500"-------
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBlank.started', textBlank.tStartRefresh)
thisExp.addData('textBlank.stopped', textBlank.tStopRefresh)

# set up handler to look after randomisation of conditions etc
testLoops = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('studyItems.xlsm'),
    seed=None, name='testLoops')
thisExp.addLoop(testLoops)  # add the loop to the experiment
thisTestLoop = testLoops.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTestLoop.rgb)
if thisTestLoop != None:
    for paramName in thisTestLoop:
        exec('{} = thisTestLoop[paramName]'.format(paramName))

for thisTestLoop in testLoops:
    currentLoop = testLoops
    # abbreviate parameter names if possible (e.g. rgb = thisTestLoop.rgb)
    if thisTestLoop != None:
        for paramName in thisTestLoop:
            exec('{} = thisTestLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "studyTest"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    polygonTest.setFillColor(shapeColor)
    # keep track of which components have finished
    studyTestComponents = [polygonTest]
    for thisComponent in studyTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    studyTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "studyTest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = studyTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=studyTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygonTest* updates
        if polygonTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonTest.frameNStart = frameN  # exact frame index
            polygonTest.tStart = t  # local t and not account for scr refresh
            polygonTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonTest, 'tStartRefresh')  # time at next scr refresh
            polygonTest.setAutoDraw(True)
        if polygonTest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygonTest.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                polygonTest.tStop = t  # not accounting for scr refresh
                polygonTest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygonTest, 'tStopRefresh')  # time at next scr refresh
                polygonTest.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in studyTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "studyTest"-------
    for thisComponent in studyTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    testLoops.addData('polygonTest.started', polygonTest.tStartRefresh)
    testLoops.addData('polygonTest.stopped', polygonTest.tStopRefresh)
    
    # ------Prepare to start Routine "blank500"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [textBlank]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank500"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blank500Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(True)
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank500"-------
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    testLoops.addData('textBlank.started', textBlank.tStartRefresh)
    testLoops.addData('textBlank.stopped', textBlank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'testLoops'


# ------Prepare to start Routine "thankYou"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
thankYouComponents = [textThanks]
for thisComponent in thankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thankYouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thankYou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thankYouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thankYouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textThanks* updates
    if textThanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textThanks.frameNStart = frameN  # exact frame index
        textThanks.tStart = t  # local t and not account for scr refresh
        textThanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textThanks, 'tStartRefresh')  # time at next scr refresh
        textThanks.setAutoDraw(True)
    if textThanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textThanks.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            textThanks.tStop = t  # not accounting for scr refresh
            textThanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textThanks, 'tStopRefresh')  # time at next scr refresh
            textThanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thankYou"-------
for thisComponent in thankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textThanks.started', textThanks.tStartRefresh)
thisExp.addData('textThanks.stopped', textThanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
