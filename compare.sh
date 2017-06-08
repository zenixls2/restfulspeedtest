#!/bin/bash

for f in *; do
	if [[ -f "$f/result" ]]; then
		echo " * $f: `tail -n2 $f/result | head -n1 | tr "Requests/sec:\t\t" " "`"
	fi
done
