# test
# example of calling mai server

import monument
import sys
from os.path import expanduser

home = expanduser("~").replace("\\","/")

# ----------------------------------------------------------------------------
# if linux, set installation folder
# otherwise leave blank
if sys.platform.startswith("linux"):
 install = home + "/MonumentDev"
else:
 install = ""

# ----------------------------------------------------------------------------
# start monument
monument.init(install)

# ----------------------------------------------------------------------------
# run models
maifile = home + "/maitest/sst.mai"
csvfile = home + "/maitest/SST.csv"
algo = "ExpSmooth(SST)"
res = monument.serve(maifile,csvfile,algo)
print(res)

