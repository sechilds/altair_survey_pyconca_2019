charts = big_dino1.json small_dino1.json anscombe_all.json unique_count1.json unique_count2.json unique_count3.json div_bar1.json div_bar2.json div_bar3.json div_bar4.json div_bar5.json div_bar6.json big_away.json big_bullseye.json big_circle.json big_dots.json big_h_lines.json big_high_lines.json big_slant_down.json big_slant_up.json big_star.json big_v_lines.json big_wide_lines.json big_x_shape.json datasaurus_all.json

all : ${charts}

data : data/long_data.csv data/response_data1.csv

serve :
	npm start

${charts}: %.json: gen_%.py
	python $<

data/long_data.csv: long_data.py
	python $<

data/response_data1.csv: response_data1.py data/long_data.csv
	python response_data1.py
