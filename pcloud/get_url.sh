#!/bin/bash

raw_page_url="https://transfer.pcloud.com/download.html?code=5Zzq2NVZ3YMKeM4xMcVZQkGNZ0q2XWGStq07tPxOLGhhd1XbwHdrV"
api_url=$(echo $raw_page_url | sed 's/transfer.pcloud.com/api.pcloud.com/; s/download.html?/\/getpublinkdownload?fileid=1\&forcedownload=1\&/')
echo $api_url
json=$(curl $api_url)
echo $json

# Parse the JSON and extract the required values
hosts=$(echo $json | jq -r '.hosts[0]')
path=$(echo $json | jq -r '.path')

# Merge the values to form the final URL
url="https://$hosts$path"
echo $url

# wget $url
filename=$(basename $url)
curl $url --output $filename

