#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <search_word> <replace_word>"
    exit 1
fi

SEARCH_WORD="$1"
REPLACE_WORD="$2"
DIRECTORY="."

# Use find to locate files and sed to perform the replacement
find "$DIRECTORY" -type f -exec sed -i "s/$SEARCH_WORD/$REPLACE_WORD/g" {} +

echo "Replacement complete."
