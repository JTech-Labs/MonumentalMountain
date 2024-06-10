all: MonumetnalMountain.py modules.py story.py story.txt
	python -m nuitka --follow-imports MonumetnalMountain.py

web: MonumetnalMountain.build/
	python -m nuitka --follow-imports MonumetnalMountain.py
	emcc MonumetnalMountain.build

clean:
	rm -r .\MonumetnalMountain.build