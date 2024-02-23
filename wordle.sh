#!/bin/bash

install_py_text="Error: Python3 is not installed, please install and try again";
help_text="usage: $(basename $0) (optional: DEBUG | HELP)";

if command -v python3 > /dev/null 2>&1; then
	echo -n "";
else
	echo "$install_py_text";
fi

if [ $# -eq 0 ]; then
	DEBUG= python3 wordle.py;
	exit "$?";
fi

if [ $# -gt 1 ]; then
	echo "$help_text";
	exit 1;
fi

case $1 in
	"DEBUG")
		python3 wordle.py DEBUG;
		exit "$?";
		;;
	"HELP")
		echo "$help_text";
		exit 0;
		;;
	*)
		echo "$help_text";
		exit 1;
		;;
esac
