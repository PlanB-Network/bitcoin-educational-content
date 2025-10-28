#!/bin/bash
# Batch generate quiz PDFs for multiple courses

# Default values
LANGUAGE="en"
OUTPUT_DIR="./output"

# Usage message
usage() {
    echo "Usage: $0 [-l language] [-o output_dir] [course1 course2 ...]"
    echo "  -l: Language code (default: en)"
    echo "  -o: Output directory (default: ./output)"
    echo ""
    echo "Examples:"
    echo "  $0 btc101 btc102 btc202"
    echo "  $0 -l fr btc101 eco204"
    echo "  $0 -l es -o ./spanish_quizzes btc101 btc102"
    exit 1
}

# Parse options
while getopts "l:o:h" opt; do
    case $opt in
        l) LANGUAGE="$OPTARG" ;;
        o) OUTPUT_DIR="$OPTARG" ;;
        h) usage ;;
        *) usage ;;
    esac
done
shift $((OPTIND-1))

# Check if any courses specified
if [ $# -eq 0 ]; then
    echo "Error: No courses specified"
    usage
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Counter for statistics
total=0
success=0
failed=0

echo "========================================"
echo "Batch Quiz PDF Generation"
echo "========================================"
echo "Language: $LANGUAGE"
echo "Output: $OUTPUT_DIR"
echo "Courses: $@"
echo "========================================"
echo ""

# Generate PDFs for each course
for course in "$@"; do
    total=$((total + 1))
    echo "[$total] Generating $course..."

    if python3 quizz_to_pdf.py "$course" -l "$LANGUAGE" -o "$OUTPUT_DIR" > /dev/null 2>&1; then
        success=$((success + 1))
        echo "    ✓ Success: ${course}_quiz_${LANGUAGE}.pdf"
    else
        failed=$((failed + 1))
        echo "    ✗ Failed: $course"
    fi
    echo ""
done

# Print summary
echo "========================================"
echo "Summary"
echo "========================================"
echo "Total courses: $total"
echo "Successful: $success"
echo "Failed: $failed"
echo "========================================"

exit $failed
