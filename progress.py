#!/usr/bin/python
import socket
from subprocess import call
from subprocess import Popen, PIPE
killp = Popen(['pidof','kweb'], stdout = PIPE)
pid = killp.communicate()[0]
call(["kill", pid.strip()])
print "Hold on for a sec, mate."
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',7007))
if result == 0:
    call(["kweb","-J","http://127.0.0.1:7007"])
else:
    import sys
    import time


    class ProgressBar:
        def __init__(self, duration):
            self.duration = duration
            self.prog_bar = '[]'
            self.fill_char = '#'
            self.width = 40
            self.__update_amount(0)

        def animate(self):
            for i in range(self.duration):
                if sys.platform.lower().startswith('win'):
                    print self, '\r',
                else:
                    print self, chr(27) + '[A'
                self.update_time(i + 1)
                time.sleep(1) 
            print self

        def update_time(self, elapsed_secs):
            self.__update_amount((elapsed_secs / float(self.duration)) * 100.0)
            self.prog_bar += '  %ds/%ss' % (elapsed_secs, self.duration)

        def __update_amount(self, new_amount):
            percent_done = int(round((new_amount / 100.0) * 100.0))
            all_full = self.width - 2
            num_hashes = int(round((percent_done / 100.0) * all_full))
            self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
            pct_place = (len(self.prog_bar) / 2) - len(str(percent_done))
            pct_string = '%d%%' % percent_done
            self.prog_bar = self.prog_bar[0:pct_place] + \
                (pct_string + self.prog_bar[pct_place + len(pct_string):])

        def __str__(self):
            return str(self.prog_bar)


    if __name__ == '__main__':

    # print a dynamic updating progress bar on one line:
    #
    #  [################100%##################]  10s/10s
    #  done
        p = Popen(['setsid','python','/home/pi/backup/ka-lite/kalite/manage.py','kaserve','host=0.0.0.0','port=7007','threads=10','daemonize=false', 'pidfile="/home/pi/backup/ka-lite/kalite/runcherrypiserver.pid"']) 
        secs = 60
        p = ProgressBar(secs)
        print 'Khan Academy is also available for free at www.khanacademy.org (hope you have fast internet).'
        print '.'
        print "Please wait while Khan Academy is starting up: that's 3500 videos totalling more than 50 GB..."

    # spawn asych (threads/processes/etc) code here that runs for secs.
    # the call to .animate() blocks the main thread.
    
        p.animate()
    
        print 'KA-Lite is ready to go!'
        call(["kweb","-J","http://127.0.0.1:7007"])
    
