

import os
import sys

assert "ASCDS_INSTALL" in os.environ, "Please setup for CIAO before installing"

# Set PYVER env variable so that it'll get replaced in setup.cfg
ver = sys.version_info
os.environ["PYVER"] = "python{}.{}".format(ver[0],ver[1]) 


from distutils.core import setup

setup( name='statmap',
       version='4.13.0',
       description='Compute a map of statistics values',
       author='Kenny Glotfelty',
       author_email='glotfeltyk@si.edu',
       url='https://github.com/kglotfelty/statmap/',
       scripts=["statmap"],
       data_files=[('param',['statmap.par'])]
                    
    )
