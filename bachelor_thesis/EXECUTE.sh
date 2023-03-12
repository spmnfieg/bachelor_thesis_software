#!/usr/bin/env bash

py scratch_predict.py &&
py scratch_inputs.py &&
sh ./scratch_rank.sh &&
py scratch_tables.py

$SHELL
