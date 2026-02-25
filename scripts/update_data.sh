#!/bin/bash
# Auto-update script for OpenAIX data
# Run this script to update rankings with latest evaluation data

set -e

echo "🔄 OpenAIX Auto-Update Pipeline"
echo "================================"

# 1. Check for new evaluation files
NEW_EVALS=$(find data/evaluations -name "*.md" -type f | wc -l)
echo "📊 Found $NEW_EVALS evaluation files"

# 2. Run standardization
python3 scripts/data_pipeline/standardize_data.py

# 3. Verify output
if [ -f "data/exports/rankings_current.json" ]; then
    SITES=$(python3 -c "import json; d=json.load(open('data/exports/rankings_current.json')); print(len(d['sites']))")
    echo "✅ Generated rankings for $SITES sites"
fi

# 4. Update timestamp
DATE=$(date +%Y-%m-%d\ %H:%M:%S)
echo "🕐 Updated at: $DATE"

echo ""
echo "✨ Data update complete!"
echo "Next steps:"
echo "  1. Test locally: python3 -m http.server 8080"
echo "  2. Commit changes: git add data/exports/ && git commit -m 'Update rankings'"
echo "  3. Push to deploy: git push origin main"
