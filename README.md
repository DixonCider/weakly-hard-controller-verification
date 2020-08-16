# Weakly-hard Controller Verification

### Step to reproduce:
0. build environment with `conda env create -f env.yaml -n weaklyhard` and activate with `conda activate weaklyhard`
1. run `make -C System-verification` to compile verifier
2. configure controller parameters in `config.yaml`
3. configure verification K value and file paths in `run.sh`
4. run `./run.sh` for verification results
