#! /usr/bin/env python

#
#  DDAA's Eleanor Margaret Burbidge Work Organizer  
#
#  Copyright 2016 by it's authors. 
#
#  Some rights reserved. See COPYING, AUTHORS.
#  This file may be used under the terms of the GNU General Public
#  License version 3.0 as published by the Free Software Foundation
#  and appearing in the file COPYING included in the packaging of
#  this file.
#
#  This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
#  WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#

"""backend.py - Backend for BWO

this class will take care of file and data base process
"""


try:
   import os
   import MDparse
   import DBparse

except ImportError as err:
   print("couldn't load module. %s" % (err))
   sys.exit(2)

class bwoBackend(object):
 def __init__(self):
   '''print('backend initialized')'''
   self.DB = DBparse.DBparser()
   self.data = MDparse.parsedData()

 def openFile(self,fileName):
   try:
      self.file = open(fileName)
   except IOError:
      return False
   return True

 def bruteParse(self):
   for line in self.file:
      print(line)

 def fieldParse(self):
   ret = self.data.parseFile(self.file)
   return ret
 
 def showParsedData(self):
   self.data.showParsedData()

 def closeFile(self):
   self.file.close()

 def cleanLine(self,text):
   text.rstrip('\r\n ')

 def cleanTitle(self,text):
   text.lstrip('#')
 #data base methods
 '''check if database exists'''
 def checkDB(self):
     status = self.DB.check('BWO.db')
     return status   
     
 '''create the basis of database''' 
 def setupDB(self):
     status = self.DB.createBlank('BWO.db')
     return status



