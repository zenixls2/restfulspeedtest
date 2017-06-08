#!/bin/bash

echo "### Test Comparison (Requests/sec)"
for f in *; do
	if [[ -f "$f/result" ]]; then
		echo " * $f: `tail -n2 $f/result | head -n1 | tr "Requests/sec:\t\t" " "`"
	fi
done

echo ""
echo "### Average Latency"
for f in *; do
	if [[ -f "$f/result" ]]; then
		echo " * $f: `tail -n10 $f/result | head -n 1 | awk '{print $2}'`"
	fi
done

echo ""
echo "### Max Latency"
for f in *; do
	if [[ -f "$f/result" ]]; then
		echo " * $f: `tail -n10 $f/result | head -n 1 | awk '{print $4}'`"
	fi
done
