# SPDX-FileCopyrightText: (C) 2023-2025 jtech-labs <~jtech-labs/public@lists.sr.ht>
#
# SPDX-License-Identifier: MIT

all:
	python -m nuitka --follow-imports MonumentalMountain.py

web:
	python -m nuitka --follow-imports MonumetnalMountain.py
	emcc MonumetnalMountain.build

clean:
	rm -r .\MonumetnalMountain.build