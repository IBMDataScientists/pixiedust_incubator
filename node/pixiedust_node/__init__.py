# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2017
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed unde
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from IPython.core.magic import (Magics, magics_class, cell_magic)
import warnings
from .nodeapp import NodeApp

@magics_class
class PixiedustNodeMagics(Magics):
    def __init__(self, shell):
        super(PixiedustNodeMagics,self).__init__(shell=shell) 

    @cell_magic
    def node(self, line, cell):
        NodeApp().run()
try:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        get_ipython().register_magics(PixiedustNodeMagics)
except NameError:
    #IPython not available we must be in a spark executor\
    pass