charts = big_dino1.json small_dino1.json anscombe_all.json

all : ${charts}

${charts}: %.json: gen_%.py
	python $<
