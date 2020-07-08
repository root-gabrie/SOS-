import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


import imaplib
import getpass


#import simpleaudio as sa

#####################################################################################################

def new_message():
	filename = 'new_message.wav'

	wave_obj = sa.WaveObject.from_wave_file(filename)
	play_obj = wave_obj.play()
	play_obj.wait_done()

	return False

def start_check(self):
	imap = imaplib.IMAP4_SSL('imap.yandex.ru')
	imap.login('support.l1@gcib.ru', 'j2Awgdj7Hj5X')

	imap.list()
	itog_message = imap.select('INBOX')

	now_message=itog_message

	if itog_message == now_message:
		now_message=imap.select('INBOX')
	else:
		new_message()


#####################################################################################################

class ScreenManagement(ScreenManager):
	pass

class Start_Programm_SOS(Screen):
	def start_chk(self):
		Clock.schedule_interval(start_check,2)
	def stop_check(self):
		
	def exit(self):
		App.get_running_app().stop()

class SOSApp(App):
	def build(self):
		Window.clearcolor = (1, 1, 1, 1)
		return ScreenManagement()

if __name__=="__main__":
	SOSApp().run()