#!/usr/bin/env python3
"""
OpenAIX SSL Fix Script
======================
Fixes SSL certificate verification issues that cause evaluation failures.

Root Cause:
-----------
The Python requests library fails SSL certificate verification on some systems,
causing all website evaluations to fail with SSLError.

Solution:
---------
1. Update CA certificates
2. Add fallback to disable SSL verification when needed
3. Add proper SSL error handling

Usage:
------
    cd /home/wesley/.openclaw/workspace/openaix-core
    source venv/bin/activate
    python3 scripts/fix_ssl_issues.py

After running this fix:
    python3 benchmark.py https://example.com
"""

import os
import sys
import subprocess

def run_command(cmd, description):
    """Run a command and report status"""
    print(f"\n📦 {description}")
    print(f"   Command: {cmd}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print(f"   ✅ Success")
            return True
        else:
            print(f"   ⚠️  Exit code: {result.returncode}")
            if result.stderr:
                print(f"   Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def fix_ssl():
    """Apply SSL fixes"""
    print("=" * 60)
    print("🔧 OpenAIX SSL Fix Tool")
    print("=" * 60)
    
    fixes_applied = []
    
    # Fix 1: Update certifi package
    if run_command("pip install --upgrade certifi", "Updating certifi package"):
        fixes_applied.append("certifi updated")
    
    # Fix 2: Install/upgrade requests and urllib3
    if run_command("pip install --upgrade requests urllib3", "Updating requests/urllib3"):
        fixes_applied.append("requests/urllib3 updated")
    
    # Fix 3: Update system CA certificates (if possible)
    print("\n📦 Updating system CA certificates")
    print("   Command: sudo update-ca-certificates (may require password)")
    result = subprocess.run(
        "sudo update-ca-certificates 2>/dev/null || echo 'Skipped'",
        shell=True,
        capture_output=True,
        text=True
    )
    if "Skipped" not in result.stdout:
        print("   ✅ System CA certificates updated")
        fixes_applied.append("system CA updated")
    else:
        print("   ⚠️  Skipped (requires sudo)")
    
    # Fix 4: Test the fix
    print("\n🧪 Testing SSL fix...")
    test_script = '''
import requests
print("Testing https://example.com...")
try:
    r = requests.get("https://example.com", timeout=10, verify=True)
    print(f"✅ SSL verification working: {r.status_code}")
except Exception as e:
    print(f"⚠️ SSL still failing, will use fallback mode: {type(e).__name__}")
'''
    
    result = subprocess.run(
        [sys.executable, "-c", test_script],
        capture_output=True,
        text=True,
        timeout=30
    )
    print(result.stdout.strip())
    if result.stderr:
        print(f"Stderr: {result.stderr.strip()}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 Fix Summary")
    print("=" * 60)
    if fixes_applied:
        for fix in fixes_applied:
            print(f"  ✅ {fix}")
    else:
        print("  ⚠️  No fixes were applied")
    
    print("\n📝 Next Steps:")
    print("  1. Test: python3 benchmark.py https://example.com")
    print("  2. If still failing, the scorer will auto-fallback to no-verify mode")
    print("  3. For production, consider fixing system SSL certificates")
    
    return len(fixes_applied) > 0

if __name__ == "__main__":
    success = fix_ssl()
    sys.exit(0 if success else 1)
