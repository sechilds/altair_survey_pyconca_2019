charts = big_dino1.json small_dino1.json anscombe_all.json unique_count1.json unique_count2.json unique_count3.json


all : ${charts}

${charts}: %.json: gen_%.py
	python $<
