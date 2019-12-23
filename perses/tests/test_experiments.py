import yaml
import numpy as np
import pickle
import os
import sys
import simtk.unit as unit
import logging
from perses.utils.data import load_smi

from perses.samplers.multistate import HybridSAMSSampler, HybridRepexSampler
from perses.annihilation.relative import HybridTopologyFactory
from perses.app.relative_setup import NonequilibriumSwitchingFEP, RelativeFEPSetup
from perses.annihilation.lambda_protocol import LambdaProtocol
from perses.rjmc.topology_proposal import TopologyProposal, SystemGenerator,SmallMoleculeSetProposalEngine
from perses.rjmc.geometry import FFAllAngleGeometryEngine

from openmmtools import mcmc
from openmmtools.multistate import MultiStateReporter, sams, replicaexchange
from perses.utils.smallmolecules import render_atom_mapping
from perses.tests.utils import validate_endstate_energies
from openmoltools import forcefield_generators
from perses.utils.openeye import *
from perses.app.utils import *
import mdtraj as md
import simtk.openmm.app as app
import simtk.openmm as openmm
from io import StringIO
import copy
from perses.app.experiments import *
#import perses dask Client
from perses.app.relative_setup import DaskClient

from unittest import skipIf
from nose.tools import raises
import os

istravis = os.environ.get('TRAVIS', None) == 'true'


ENERGY_THRESHOLD = 1e-4
from openmmtools.constants import kB

def test_BuildProposalNetwork():
    """
    test BuildProposalNetwork with default arguments
    """
    _simulation_parameters = {(0,1): {'complex': ('smc', {'timestep': 1 * unit.femtoseconds}), 'solvent': ('repex', {'timestep': 1*unit.femtoseconds})},
                              (1,0): {'solvent': ('sams', {'timestep': 2 * unit.femtoseconds, 'splitting': "V R O R V"})}
                             }
    network = BuildProposalNetwork(ligand_input = os.path.join(os.getcwd(), '../../examples/mcl1-example/MCL1_ligands.sdf'),
                                   ligand_indices = [4,6],
                                   receptor_filename = os.path.join(os.getcwd(), '../../examples/mcl1-example/MCL1_protein_fixed.pdb'),
                                   graph_connectivity = 'fully_connected',
                                   cost = None,
                                   resources = None,
                                   proposal_parameters = None,
                                   simulation_parameters = _simulation_parameters)
    network.create_network()
    print(vars(network))
    return network

if __name__ == "__main__":
    test_BuildProposalNetwork()