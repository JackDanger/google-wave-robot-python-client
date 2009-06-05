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


def OnSelfAdded(properties, context):
  """Invoked when Dummy is first added to the wave."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Hello there!")
  blip = context.GetBlipById(root_wavelet.GetRootBlipId())
  blip.GetDocument().AppendInlineBlip()

if __name__ == '__main__':
  dummy = robot.Robot(ROBOT_NAME.capitalize(),
                      '1',
                      image_url='/public/%s.png' % ROBOT_NAME,
                      profile_url='_wave/profile.xml')
  dummy.RegisterHandler(events.WAVELET_SELF_ADDED,
                        OnSelfAdded)
  dummy.Run(debug=True)
