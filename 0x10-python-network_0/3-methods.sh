#!/bin/bash
# script that takes in a URL and displays all HTTP methods
curl -Is "$1" | grep Allow | cut -c 8-
