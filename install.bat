@REM 修改版本号可以更新到任意版本
@set xcore_version=0.3.2
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