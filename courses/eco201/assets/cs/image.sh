#!/bin/bash

# Script to duplicate an image and shift subsequent images

echo "=========================================="
echo "IMAGE DUPLICATOR AND SHIFTER"
echo "=========================================="
echo ""

# Check if we have images in the current directory
if ! ls *.webp >/dev/null 2>&1; then
    echo "❌ No .webp files found in current directory!"
    exit 1
fi

# Display current images
echo "Current images in directory:"
ls -1 *.webp | sort
echo ""

# Ask which image to duplicate
read -p "Enter the image number to duplicate (e.g., 018): " IMAGE_NUM

# Validate input
if [[ ! "$IMAGE_NUM" =~ ^[0-9]{3}$ ]]; then
    echo "❌ Please enter a 3-digit number (e.g., 018)"
    exit 1
fi

SOURCE_FILE="${IMAGE_NUM}.webp"

# Check if source file exists
if [[ ! -f "$SOURCE_FILE" ]]; then
    echo "❌ File $SOURCE_FILE not found!"
    exit 1
fi

# Calculate the next number
NEXT_NUM=$((10#$IMAGE_NUM + 1))
NEXT_NUM_FORMATTED=$(printf "%03d" $NEXT_NUM)

echo ""
echo "Plan:"
echo "1. Rename existing images from ${NEXT_NUM_FORMATTED}.webp onwards (in reverse order)"
echo "2. Copy $SOURCE_FILE to ${NEXT_NUM_FORMATTED}.webp"
echo ""
read -p "Proceed? (y/n): " CONFIRM

if [[ "$CONFIRM" != "y" && "$CONFIRM" != "Y" ]]; then
    echo "Operation cancelled."
    exit 0
fi

echo ""
echo "Starting operation..."
echo ""

# Find the highest numbered file
HIGHEST=$(ls *.webp 2>/dev/null | sed 's/\.webp$//' | sort -n | tail -1)

if [[ -z "$HIGHEST" ]]; then
    echo "❌ Could not determine highest numbered file"
    exit 1
fi

# Rename files in reverse order to avoid conflicts
for ((i=10#$HIGHEST; i>=10#$NEXT_NUM; i--)); do
    OLD_NUM=$(printf "%03d" $i)
    NEW_NUM=$(printf "%03d" $((i + 1)))
    OLD_FILE="${OLD_NUM}.webp"
    NEW_FILE="${NEW_NUM}.webp"
    
    if [[ -f "$OLD_FILE" ]]; then
        mv "$OLD_FILE" "$NEW_FILE"
        echo "✓ Renamed: $OLD_FILE -> $NEW_FILE"
    fi
done

# Copy the source file to create the duplicate
cp "$SOURCE_FILE" "${NEXT_NUM_FORMATTED}.webp"
echo "✓ Duplicated: $SOURCE_FILE -> ${NEXT_NUM_FORMATTED}.webp"

echo ""
echo "=========================================="
echo "Operation complete!"
echo "=========================================="
echo ""
echo "Updated images:"
ls -1 *.webp | sort