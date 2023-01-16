#!/bin/bash
# Sends a DELETE request to the RUL passed as the first argument, and displays the body of the response
curl -s -o -X DELETE "$1"
