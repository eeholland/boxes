#!/usr/bin/env python3
# Copyright (C) 2013-2014 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *


class DisplayFrame(Boxes):
    """Frame for displaying other laser cut sheets"""

    ui_group = "Tray"

    def __init__(self):
        Boxes.__init__(self)
        self.buildArgParser("x", "y", "h", "outside")

    def render(self):

        # if self.outside:
        #     self.sx = self.adjustSize(self.sx, False, False)
        #     self.sy = self.adjustSize(self.sy, False, False)

        x = self.x
        y = self.y
        h = self.h
        t = self.thickness


        # Inner walls
        self.rectangularWall(x,y)
        # for i in range(len(self.sx) - 1):
        #     e = [edges.SlottedEdge(self, self.sy, slots=0.5 * h), "e", "e", "e"]
        #     self.rectangularWall(y, h, e, move="up")

        # for i in range(len(self.sy) - 1):
        #     e = ["e", "e", edges.SlottedEdge(self, self.sx[::-1], "e", slots=0.5 * h), "e"]
        #     self.rectangularWall(x, h, e, move="up")



