charts = big_dino1.json small_dino1.json anscombe_all.json unique_count1.json unique_count2.json unique_count3.json


all : ${charts} data/long_data.csv data/response_data1.csv

${charts}: %.json: gen_%.py
	python $<

data/long_data.csv: long_data.py
	python $<

data/response_data1.csv: response_data1.py data/long_data.csv
	python response_data1.py
