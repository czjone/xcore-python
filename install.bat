@REM 修改版本号可以更新到任意版本
@set xcore_version=0.3.7
@set filename=xcore-%xcore_version%
@set liburl="https://github.com/czjone/xcore-python/releases/download/%xcore_version%/%filename%.tar.gz"
@curl -O -L %liburl%
@tar -zxvf %filename%.tar.gz
@cd %filename%
@python step.py install
@cd ..
@del %filename%.tar.gz
@rd /s/q build
@rd /s/q %filename%

@REM @set filename=translator-%xcore_version%
@REM @set liburl="https://github.com/czjone/xcore-python/releases/download/%xcore_version%/%filename%.tar.gz"
@REM @curl -O -L %liburl%
@REM @tar -zxvf %filename%.tar.gz
@REM @cd %filename%
@REM @python step.py install
@REM @cd ..
@REM @del %filename%.tar.gz
@REM @rd /s/q build
@REM @rd /s/q %filename%

@pip uninstall googletrans
@cd src/googletrans
@python setup.py install
@cd ../../
