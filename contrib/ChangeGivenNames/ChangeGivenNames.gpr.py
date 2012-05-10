#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009 Benny Malengier
# Copyright (C) 2011 Doug Blank <doug.blank@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id: $

"""
GRAMPS registration file
"""

#------------------------------------------------------------------------
#
# Fix Capitalization of Given Names
#
#------------------------------------------------------------------------

register(TOOL, 
id    = 'chgivenname',
name  = _("Fix Capitalization of Given Names"),
description =  _("Searches the entire database and attempts to "
                    "fix capitalization of the given names."),
version = '1.0.7',
gramps_target_version = '3.5',
status = STABLE,
fname = 'ChangeGivenNames.py',
authors = ["Donald N. Allingham", "Doug Blank"],
authors_email = ["don@gramps-project.org", "doug.blank@gmail.com"],
category = TOOL_DBPROC,
toolclass = 'ChangeGivenNames',
optionclass = 'ChangeGivenNamesOptions',
tool_modes = [TOOL_MODE_GUI]
  )