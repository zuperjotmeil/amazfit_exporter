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
	lstupdtime = lstupd_f.read()
	lstupd_f.close()

print ('The last time it was updated: '+ str(lstupdtime) + ' current time is: ' + str(curtime))
upd_begtime = input('Press <Enter> to accept, 0 to sync everything>>') or lstupdtime
print (upd_begtime)

amazfit_exporter.db_to_tcx(db,dest,upd_begtime)

# Complete without crashing, so update the last update file for next time
lstupd_f = open(lstupd_file,'w')
lstupd_f.write(str(curtime))
lstupd_f.close()
