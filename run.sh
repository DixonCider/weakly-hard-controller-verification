#!/bin/bash
CONFIG_FILE="config.yaml"
VERIFIER="System-verification/verifier"
FSM_FILE="controller.in"
K="14"
CM_FILE="cost_matrix.csv"
BOUNDARY_FILE="boundary.csv"
python generate_controller_automaton.py $CONFIG_FILE $FSM_FILE
$VERIFIER weaklyhardsingle $FSM_FILE $K $CM_FILE $BOUNDARY_FILE
$VERIFIER weaklyhardreuse $FSM_FILE $K
python experiment_fusion.py $K $BOUNDARY_FILE $CM_FILE
rm $BOUNDARY_FILE $CM_FILE $FSM_FILE
