import os
import subprocess
from pydub import AudioSegment

class VoiceChannel:
    def __init__(self):
        self.conf = {
            "voice_configs": {
                "htsvoice_resource": "/usr/local/Cellar/open-jtalk/1.11/voice/",
                "jtalk_dict": "/usr/local/Cellar/open-jtalk/1.11/dic"
            }
        }


    def creat_WAV(self, text, filepath='voice_message', voicetype='mei', emotion='normal'):
        htsvoice = {
            'mei': {
                'normal': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'mei/mei_normal.htsvoice')],
                'angry': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'mei/mei_angry.htsvoice')],
                'bashful': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'mei/mei_bashful.htsvoice')],
                'happy': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'mei/mei_happy.htsvoice')],
                'sad': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'mei/mei_sad.htsvoice')]
            },
            'm100': {
                'normal': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'm100/nitech_jp_atr503_m001.htsvoice')]
            },
            'tohoku-f01': {
                'normal': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'htsvoice-tohoku-f01-master/tohoku-f01-neutral.htsvoice')],
                'angry': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'htsvoice-tohoku-f01-master/tohoku-f01-angry.htsvoice')],
                'happy': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'htsvoice-tohoku-f01-master/tohoku-f01-happy.htsvoice')],
                'sad': ['-m', os.path.join(self.conf['voice_configs']['htsvoice_resource'], 'htsvoice-tohoku-f01-master/tohoku-f01-sad.htsvoice')]
            }
        }

        open_jtalk = ['open_jtalk']
        mech = ['-x', self.conf['voice_configs']['jtalk_dict']]
        speed = ['-r', '1.0']
        outwav = ['-ow', filepath+'.wav']
        cmd = open_jtalk + mech + htsvoice[voicetype][emotion] + speed + outwav
        c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        c.stdin.write(text.encode())
        c.stdin.close()
        c.wait()
        audio_segment = AudioSegment.from_wav(filepath+'.wav')
        os.remove(filepath+'.wav')
        audio_segment.export(filepath+'.mp3', format='mp3')
        return filepath+'.mp3'

    def after_play(self, e):
        print(e)
