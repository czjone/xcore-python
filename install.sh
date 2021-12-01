xcore_version="0.3.1"
## 显示错误
function error(){
	local msg=$1
	if [[ ${msg} != '' ]]; then
		echo -e "[\033[31mERROR\033[0m] "$1
	fi
}

##显示调试信息
function debug(){
	local msg=$1
	if [[ ${msg} != '' ]]; then
		echo -e "[\033[34mMESSAGE\033[0m] "$1
	fi
}

##显示成功的信息
function ok() {
	local msg=$1
	if [[ ${msg} != '' ]]; then
		echo -e "[\033[32mOK\033[0m] "$1
	fi
}

## 检查上一条命令的执行结果
function checkResult(){
	local ret=$1
	local successMsg=$2
	local errormsg=$3
	if [[ ${ret} != 0 ]]; then
		error ${errormsg}
		return ${ret}
	else
		ok ${successMsg}
		return 0
	fi
}

## 检查上一条命令的反选结果。如果检查到有失败的消息就停止执行后面的任务
function checkResultAndEchoFailMsgAndExit(){
	local ret=$1
	if [[ ${ret} != 0 ]]; then 
		echo -e "[\033[31mERROR\033[0m] "$2 #用通用函数会导致数据显示的数据不完整。我也不知道是为什么。
		exit ${ret}
	fi
}

filename="xcore-$xcore_version"
liburl="https://github.com/czjone/xcore-python/releases/download/${xcore_version}/$filename.tar.gz"
debug "下载:$liburl"
curl -O -L $liburl
checkResultAndEchoFailMsgAndExit $? "下载 $liburl 失败"
tar -zxvf $filename.tar.gz
checkResultAndEchoFailMsgAndExit $? "解压 $filename 失败"
cd $filename
python3 step.py install
cd ..
checkResultAndEchoFailMsgAndExit $? "更新 $xcore_version 失败!"
rm -rf $filename.tar.gz
debug "更新 $xcore_version 成功!"