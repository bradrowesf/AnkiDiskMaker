from notetranslator import NoteTranslator

class MidiStringMaker(object):

	def __init__(self, translator):
	
		self.myTranslator = translator
		self.myKeyDown = str(90)
		self.myKeyUp = str(80)
		self.myVelocity = str(60)
		self.ticksPerBeat = 960
		
	def AppendNote(self, note, placement, duration):
		# note - pitch to add
		# placement - beats following last event
		# duration - beats note held
		
		keyDown =  self.KeyDown(note, placement)
		keyUp = self.KeyUp(note, duration)
		outString = keyDown + keyUp
		
		return outString
	
	def AppendChord(self, notes, placement, duration):
		# notes - arrau of pitches to add
		# placement - beats following last event
		# duration - beats note held

		chordDown = self.ChordDown( notes, placement)
		chordUp = self.ChordUp( notes, duration)
		outString = chordDown + chordUp
		
		return outString
	
	def KeyDown(self, note, placement, newline = True):
		# note - pitch to add
		# placement - beats following last event

		outString = "E "	# starts w/ this for some reason
		outString += str(self.ticksPerBeat*placement) + " "	# 960 per beat
		outString += self.myKeyDown + " "	# note down
		outString += self.myTranslator.GetHexString(note) + " "
		outString += self.myVelocity # velocity
		if newline==True:
			outString += '\n' 
		
		return outString
		
	def KeyUp(self, note, placement, newline = True):
		# note - pitch to add
		# placement - beats following last event
		
		outString = "E "	# starts w/ this for some reason
		outString += str(self.ticksPerBeat*placement) + " "	# 960 per beat
		outString += self.myKeyUp + " "	# note up
		outString += self.myTranslator.GetHexString(note) + " "
		outString += self.myVelocity  # velocity
		if newline==True:
			outString += '\n'
		
		return outString
		
	def ChordDown(self, notes, placement, newline = True):
		# a string for each note in notes
		
		outString = ""
		for note in notes:
			outString += self.KeyDown( note, placement, newline)
			
		return outString
		
	def ChordUp(self, notes, placement, newline = True):
		# a string for each note in notes
		
		outString = ""
		for note in notes:
			outString += self.KeyUp( note, placement, newline)
			
		return outString
	
	
		
#test code
if __name__ == "__main__":
	t = NoteTranslator()
	sm = MidiStringMaker(t)
	
	notes = []
	notes.append(t.GetMidiCodeForHumans("Bb5"))
	notes.append(t.GetMidiCodeForHumans("G#2"))
	notes.append(t.GetMidiCodeForHumans("D4"))
	
	
	print sm.AppendChord( notes, 3, 7)