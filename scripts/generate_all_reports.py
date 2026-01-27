#!/usr/bin/env python3
"""
Master Report Generator

Runs all overview report generators and creates all HTML reports in one go.

Usage:
    python generate_all_reports.py

This will generate:
1. Video Deployment Overview
2. Image Translation Overview
3. Markdown Translation Overview
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime

def run_script(script_path, description):
    """Run a Python script and return success status."""
    print(f"\n{'='*60}")
    print(f"🚀 {description}")
    print(f"{'='*60}\n")

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=script_path.parent,
            capture_output=False,
            text=True
        )

        if result.returncode == 0:
            print(f"\n✅ {description} completed successfully!")
            return True
        else:
            print(f"\n❌ {description} failed with exit code {result.returncode}")
            return False

    except Exception as e:
        print(f"\n❌ Error running {description}: {e}")
        return False

def main():
    """Main execution function."""
    print("=" * 60)
    print("🎯 Master Report Generator")
    print("=" * 60)
    print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    script_dir = Path(__file__).parent.resolve()

    # Define all scripts to run
    scripts = [
        {
            'path': script_dir / 'video_deployment_overview' / 'generate_report.py',
            'description': 'Video Deployment Overview'
        },
        {
            'path': script_dir / 'image_translation_overview' / 'generate_report.py',
            'description': 'Image Translation Overview'
        },
        {
            'path': script_dir / 'md_translation_overview' / 'generate_report.py',
            'description': 'Markdown Translation Overview'
        }
    ]

    # Verify all scripts exist
    missing_scripts = []
    for script_info in scripts:
        if not script_info['path'].exists():
            missing_scripts.append(script_info['path'])

    if missing_scripts:
        print("❌ Error: The following scripts were not found:")
        for script in missing_scripts:
            print(f"   - {script}")
        return 1

    # Run all scripts
    results = []
    for script_info in scripts:
        success = run_script(script_info['path'], script_info['description'])
        results.append({
            'description': script_info['description'],
            'success': success,
            'path': script_info['path']
        })

    # Print summary
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)

    all_successful = True
    for result in results:
        status = "✅ SUCCESS" if result['success'] else "❌ FAILED"
        print(f"{status} - {result['description']}")
        if not result['success']:
            all_successful = False

    print("\n" + "=" * 60)
    print("📁 Generated Reports")
    print("=" * 60)

    # List generated HTML files (all in central reports folder)
    reports_dir = script_dir / 'reports'
    html_files = [
        reports_dir / 'video_deployment_overview.html',
        reports_dir / 'image_translation_overview.html',
        reports_dir / 'md_translation_overview.html'
    ]

    for html_file in html_files:
        if html_file.exists():
            size = html_file.stat().st_size / 1024  # Size in KB
            print(f"✓ {html_file.name}")
            print(f"  └─ {html_file} ({size:.1f} KB)")
        else:
            print(f"✗ {html_file.name} (not found)")

    print()
    print(f"📅 Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    if all_successful:
        print("\n🎉 All reports generated successfully!")
        print("\n💡 Tip: Open the HTML files in your browser to view the reports.")
        return 0
    else:
        print("\n⚠️  Some reports failed to generate. Check the output above for details.")
        return 1

if __name__ == '__main__':
    exit(main())
