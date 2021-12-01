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

# apktool version2.4.0 下载安装: https://ibotpeaches.github.io/Apktool/install/
# 文档 https://ibotpeaches.github.io/Apktool/documentation/
apkname=test
java -jar apktool.jar d ${apkname}.apk
java -jar apktool.jar b ${apkname} -o ${apkname}1.apk
# rm -rf ${apkname}


# cmd=$1
# insrc=$2
# outsrc=$3

# if [[ $cmd == "-dapk" ]]; then
# 	echo 解包APK
# elif [[ $cmd == "-capk" ]]; then
# 	echo 打包apk
# else
# 	echo 不知道做什么
# fi

# # ./flatc -o build/cpp -c --gen-object-api files
# # generated android message code.
# sdk_android="../../xv-sdk-android/xv-sdk-adapter/src/main/java/"
# ./mac-flatc -o ${sdk_android} -j ../APP2Native.fbs ../Native2APP.fbs ../Native2Server.fbs ../Server2Native.fbs ../Errors.fbs
# checkResultAndEchoFailMsgAndExit $? "生成java失败"
# ok "生成java成功:${sdk_android}"
# ok ">>>>>>>>>>> 处理完成 >>>>>>>>"