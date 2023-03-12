#!/usr/bin/env bash

echo "Ranking sampling policies evaluated on all 6 learners (Table IV and Table V individual rankings) using inputs (txt files) in ./output/table4/ and ./output/table5/"

cat ./output/table4/zbrier.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_brier.csv

echo "1 of 14 csv files generated"

cat ./output/table4/zd2h.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_d2h.csv

echo "2 of 14 csv files generated"

cat ./output/table4/zrecall.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_recall.csv

echo "3 of 14 csv files generated"

cat ./output/table4/zpf.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_pf.csv

echo "4 of 14 csv files generated"

cat ./output/table4/zroc_auc.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_auc.csv

echo "5 of 14 csv files generated"

cat ./output/table4/zifa.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_ifa.csv

echo "6 of 14 csv files generated"

cat ./output/table4/zgm.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_gm.csv

echo "7 of 14 csv files generated"

cat ./output/table5/zbrier.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_brier.csv

echo "8 of 14 csv files generated"

cat ./output/table5/zd2h.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_d2h.csv

echo "9 of 14 csv files generated"

cat ./output/table5/zrecall.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_recall.csv

echo "10 of 14 csv files generated"

cat ./output/table5/zpf.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_pf.csv

echo "11 of 14 csv files generated"

cat ./output/table5/zroc_auc.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_auc.csv

echo "12 of 14 csv files generated"

cat ./output/table5/zifa.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_ifa.csv

echo "13 of 14 csv files generated"

cat ./output/table5/zgm.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_gm.csv


cat ./output/table5/zfn.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_fn.csv
cat ./output/table5/zfp.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_fp.csv
cat ./output/table5/ztn.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_tn.csv
cat ./output/table5/ztp.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table5/scratch_table5_tp.csv

cat ./output/table4/zfn.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_fn.csv
cat ./output/table4/zfp.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_fp.csv
cat ./output/table4/ztn.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_tn.csv
cat ./output/table4/ztp.txt | py -2.7 run_scott_knott.py --text 30 --latex False > ./output/table4/scratch_table4_tp.csv



echo "7 csv files generated in ./output/table4/ and 7 csv files generated in ./output/table5/"



