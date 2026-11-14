#!/usr/bin/env python3
"""
Build script to compile GitPatch Wave into a standalone desktop executable using PyInstaller.

Usage:
    python scripts/build_exe.py
"""

import os
import sys
import subprocess


def build():
    """Execute PyInstaller build with all required assets bundled."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)

    # Path separator for PyInstaller --add-data differs between Windows and Unix
    sep = ';' if sys.platform.startswith('win') else ':'

    templates_arg = f'templates{sep}templates'
    static_arg = f'static{sep}static'

    cmd = [
        sys.executable,
        '-m',
        'PyInstaller',
        '--onefile',
        '--name', 'GitPatchWave',
        '--add-data', templates_arg,
        '--add-data', static_arg,
        '--hidden-import', 'jinja2',
        '--hidden-import', 'numpy',
        'app.py'
    ]

    print("Building GitPatch Wave standalone executable...")
    print("Command:", " ".join(cmd))
    
    result = subprocess.run(cmd)
    if result.returncode == 0:
        print("\nBuild successful!")
        dist_path = os.path.join(project_root, 'dist', 'GitPatchWave.exe' if sys.platform.startswith('win') else 'GitPatchWave')
        print(f"Executable output: {dist_path}")
    else:
        print(f"\nBuild failed with exit code {result.returncode}")
        sys.exit(result.returncode)


if __name__ == '__main__':
    build()
