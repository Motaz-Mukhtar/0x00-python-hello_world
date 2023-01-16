#!/bin/bash
# Sends a request to the URL, and displays the size of the body
curl -s -i "$1" | grep Content-Length | cut -b 17- 
