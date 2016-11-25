#####################################################################
# -*- coding: iso-8859-1 -*-                                        #
#                                                                   #
# Frets on Fire                                                     #
# Copyright (C) 2006 Sami Kyöstilä                                  #
#                                                                   #
# This program is free software; you can redistribute it and/or     #
# modify it under the terms of the GNU General Public License       #
# as published by the Free Software Foundation; either version 2    #
# of the License, or (at your option) any later version.            #
#                                                                   #
# This program is distributed in the hope that it will be useful,   #
# but WITHOUT ANY WARRANTY; without even the implied warranty of    #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
# GNU General Public License for more details.                      #
#                                                                   #
# You should have received a copy of the GNU General Public License #
# along with this program; if not, write to the Free Software       #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,        #
# MA  02110-1301, USA.                                              #
#####################################################################

import unittest
from GameEngine import GameEngine
from Dialogs import getText
from View import Layer

class TestLayer(Layer):
  def __init__(self, engine):
    self.text = None
    self.engine = engine


  def run(self, ticks):
    """
    This next control structure is responsible
    to ensure that there is some text at the
    moment in the unit test of dialogues is called.
    If there are no texts she passes a standard text.
    Is next control structure uses existence
    of the value of the size of the texture to
    This is converted and used at the time
    in the screen need to be drawn.
    """
    if not self.text:
      self.text = "tmp"
      self.text = getText(self.engine, "Enter name:", "Wario")
    else:
      pass

class DialogTestInteractive(unittest.TestCase):
  def testGetTest(self):
    text = getText(self.e, "Please enter your name:", "Wario")

  def setUp(self):
    self.e = GameEngine()

  def tearDown(self):
    self.e.quit()

"""
This next control structure check whether
to start the unit tests on the main of the game.
"""
if __name__ == "__main__":
  unittest.main()
else:
  pass