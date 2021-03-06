from nose.tools import *
from DeckMaker.midistringmaker import MidiStringMaker
from DeckMaker.notetranslator import NoteTranslator

class TestMidiStringMaker(object):
    
	def __init__(self):

		self.t = NoteTranslator()
		self.sm = MidiStringMaker(self.t)
	
 	def test_KeyDown(self):
		assert_equal(self.sm.KeyDown( self.t.GetMidiCodeForHumans("E5"), 3), "E 2880 90 40 60\n")
		assert_equal(self.sm.KeyDown( self.t.GetMidiCodeForHumans("D#2"), 17), "E 16320 90 1b 60\n")
		
	def test_KeyUp(self):
		assert_equal(self.sm.KeyUp( self.t.GetMidiCodeForHumans("G#4"), 2), "E 1920 80 38 60\n")
		assert_equal(self.sm.KeyUp( self.t.GetMidiCodeForHumans("D#2"), 17), "E 16320 80 1b 60\n")

	def test_AppendNote(self):
		assert_equal(self.sm.AppendNote( self.t.GetMidiCodeForHumans("E#5"), 12, 3), "E 11520 90 41 60\nE 2880 80 41 60\n")
		assert_equal(self.sm.AppendNote( self.t.GetMidiCodeForHumans("A#2"), 3, 7), "E 2880 90 22 60\nE 6720 80 22 60\n")
		
	def GetChordNotes( self, humanNotes):
		# Utility method for Chord Tests
	
		outNotes = []
		for note in humanNotes:
			outNotes.append(self.t.GetMidiCodeForHumans(note))
			
		return outNotes
	
	def test_ChordDown(self):
		notes = self.GetChordNotes(["Gb5","C#2","A3"])
		assert_equal(self.sm.ChordDown( notes, 2), "E 1920 90 42 60\nE 0 90 19 60\nE 0 90 2d 60\n")
		
		notes = self.GetChordNotes(["A#2","F2","E4"])
		assert_equal(self.sm.ChordDown( notes, 3), "E 2880 90 22 60\nE 0 90 1d 60\nE 0 90 34 60\n")
	
		notes = self.GetChordNotes(["Cb5","C#2","G7"])
		assert_equal(self.sm.ChordDown( notes, 5), "E 4800 90 3b 60\nE 0 90 19 60\nE 0 90 5b 60\n")

	def test_ChordUp(self):
		notes = self.GetChordNotes(["Gb5","C#2","A3"])
		assert_equal(self.sm.ChordUp( notes, 4), "E 3840 80 42 60\nE 0 80 19 60\nE 0 80 2d 60\n")
		
		notes = self.GetChordNotes(["A#2","F2","E4"])
		assert_equal(self.sm.ChordUp( notes, 7.5), "E 7200 80 22 60\nE 0 80 1d 60\nE 0 80 34 60\n")
	
		notes = self.GetChordNotes(["Cb5","C#2","G7"])
		assert_equal(self.sm.ChordUp( notes, 3.5), "E 3360 80 3b 60\nE 0 80 19 60\nE 0 80 5b 60\n")
	
	def test_AppendChord(self):
	
		notes = self.GetChordNotes(["Cb5","C#2","G7"])
		assert_equal(self.sm.AppendChord( notes, 3.5, 2),"E 3360 90 3b 60\nE 0 90 19 60\nE 0 90 5b 60\nE 1920 80 3b 60\nE 0 80 19 60\nE 0 80 5b 60\n")