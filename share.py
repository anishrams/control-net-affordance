import config
from cldm.hack import disable_verbosity, enable_sliced_attention
import sys
sys.path.append("/proj/control-net-affordance/")

disable_verbosity()

if config.save_memory:
    enable_sliced_attention()
