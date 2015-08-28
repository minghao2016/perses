"""
This file contains the base class to calculate weights for each
state
"""

class StateWeight(object):
    """
    Provides facilities for calculating the weight of a given state
    (such as a molecule, or mutant). 
    """
    
    def __init__(self):
        pass

    @staticmethod
    def log_weight(sampler_state):
        """
	Calculate the log-weight for a given state
	
	Arguments
	---------
	sampler_state : SamplerState namedtuple
            Contains the system, topology, positions, metadata
	    for the system relevant to weight calculation
	"""
        return 0
