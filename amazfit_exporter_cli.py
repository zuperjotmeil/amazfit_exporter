#!/usr/bin/python3
import sys
import amazfit_exporter
import datetime
import time
import os

db = sys.argv[1]
dest = sys.argv[2]
curtime = round(time.time()*1000)
lstupdtime = 0

lstupd_file = dest+'\lstupd.txt'
if os.path.exists(lstupd_file):
	lstupd_f = open(lstupd_file,'r')
	lstupdtime = int(lstupd_f.read())
	lstupd_f.close()

updtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(lstupdtime/1000)))
print ('The last time it was sync: '+ str(updtime))
upd_begtime = input('Press <Enter> to accept, 0 to resync everything>>') or lstupdtime
#print (upd_begtime)

amazfit_exporter.db_to_tcx(db,dest,upd_begtime)

# Complete without crashing, so update the last update file for next time
lstupd_f = open(lstupd_file,'w')
lstupd_f.write(str(int(curtime)))
lstupd_f.close()
