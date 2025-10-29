#!/bin/sh
python -m nuitka --onefile --run --plugin-enable=anti-bloat --plugin-enable=numpy --plugin-enable=pylint-warnings --windows-company-name="arro productions" --windows-product-n
ame="flappy amongus" --windows-file-version="1.1.2" --windows-product-version="1.1.2" --windows-file-description="flap as the bean we know as amongus" --windows-icon-from-ico="icons/icon.ico" --include-data-dir=Sounds=Sounds/ --include-data-dir=Graphics=G
raphics/ --include-data-file="libmpg123-0.dll=libmpg123-0.dll" --clang main.py
