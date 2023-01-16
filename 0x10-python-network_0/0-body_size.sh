#!/usr/bin/env bash

curl -s -i "$1" | grep Content-Length | cut -b 17- 
