import pickle
import numpy as np
from time import time
import sys

from formal_verification_under_WH_constraints.mock_single_verifier import BoundSingleVerifier
from formal_verification_under_WH_constraints.monotonic_verifier import MonotonicVerifier
from formal_verification_under_WH_constraints.probe_verifier import ProbeVerifier
from shortcut_verifier import ShortcutVerifier
from lfs_heuristic_verifier import LFSHeuristicVerifier

def evaluate_pv_and_mv(k_bar, boundary, cost_matrix):

    single_v = BoundSingleVerifier(k_bar, boundary)
    pv = ProbeVerifier(k_bar, single_v, cost_matrix)
    mv = MonotonicVerifier(k_bar, single_v, cost_matrix)
    sv = ShortcutVerifier(k_bar, single_v, cost_matrix)
    lv = LFSHeuristicVerifier(k_bar, single_v, cost_matrix)

    start_t = time()
    pv_trace, pv_cost = pv.verify_all(print_process=False, 
                                      use_cost_matrix=False, 
                                      use_interpol_prob=False, 
                                      account_others=False)
    pv_time = 1000 * (time() - start_t)

    start_t = time()
    mv_trace, mv_cost = mv.verify_all(print_process=False)
    mv_time = 1000 * (time() - start_t)

    start_t = time()
    sv_trace, sv_cost = sv.verify_all()
    sv_time = 1000 * (time() - start_t)

    start_t = time()
    lv_trace, lv_cost = lv.verify_all()
    lv_time = 1000 * (time() - start_t)

    # return pv_time, mv_time
    print('Traces:')
    print('\tprobe', pv_trace)
    print('\tmonotonic', mv_trace)
    print('\tshortcut', sv_trace)
    print('\tlfs_heuristic', lv_trace)
    return pv_cost, mv_cost, sv_cost, lv_cost

def main():
    k_bar = int(sys.argv[1])
    boundary_csv = sys.argv[2]
    cost_matrix_csv = sys.argv[3]

    boundary = np.genfromtxt(boundary_csv, delimiter=',')
    cost_matrix = np.genfromtxt(cost_matrix_csv, delimiter=',')

    pv_time, mv_time, sv_time, lv_time = evaluate_pv_and_mv(k_bar, boundary, cost_matrix)
    print('Runtimes:')
    print('\tbrute_force', np.sum(cost_matrix))
    print('\tprobe', pv_time)
    print('\tmonotonic', mv_time)
    print('\tshortcut', sv_time)
    print('\tlfs_heuristic', lv_time)

if __name__ == '__main__':
    main()
