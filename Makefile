all:
	python -m nuitka --follow-imports MonumentalMountain.py

web:
	python -m nuitka --follow-imports MonumetnalMountain.py
	emcc MonumetnalMountain.build

clean:
	rm -r .\MonumetnalMountain.build