@pip uninstall googletrans
@cd src/googletrans
@python setup.py install
@cd ../../

@python step.py sdist
@python step.py install
@rd /s/q build
@REM @rd /s/q dist
@del /s/q MANIFEST
@pause