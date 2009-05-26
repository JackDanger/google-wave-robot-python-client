#!/usr/bin/python2.4
#
# Copyright 2009 Google Inc. All Rights Reserved.
"""Implementation of Dummy robot."""

__author__ = 'davidbyttow@google.com (David Byttow)'


import logging

from api import events
from api import model
from api import robot

# Globals
ROBOT_NAME = 'dummy'
LOCAL_NAME = 'davidb'


def IsRobotInList(l):
  """Determines if this robot is in the participant list."""
  for participant in l:
    if participant.startswith(ROBOT_NAME) or participant.startswith(LOCAL_NAME):
      return True
  return False


def OnParticipantsChanged(properties, context):
  """Invoked when any participants have been added/removed from the wavelet."""
  added = properties['participantsAdded']
  if IsRobotInList(added):
    Setup(context)


def Setup(context):
  """Called when this robot is first added to the wave."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Hello there!")
  blip = context.GetBlipById(root_wavelet.GetRootBlipId())
  blip.GetDocument().AppendInlineBlip()

if __name__ == '__main__':
  dummy = robot.Robot(ROBOT_NAME.capitalize(),
                      image_url='/public/%s.png' % ROBOT_NAME,
                      profile_url='_wave/profile.xml')
  dummy.RegisterHandler(events.WAVELET_PARTICIPANTS_CHANGED,
                        OnParticipantsChanged)
  dummy.Run(debug=True)
