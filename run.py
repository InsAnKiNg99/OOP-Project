#!/usr/bin/env python3
"""
UOT Admission Portal - Setup and Run Script
This script sets up and runs the Flask application
"""

import os
import sys
import subprocess
import platform

def run_command(command, description=""):
    """Run a command and handle errors"""
    if description:
        print(f"\n{'='*50}")
        print(f"  {description}")
        print(f"{'='*50}")
    try:
        result = subprocess.run(command, shell=True, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: Command failed with return code {e.returncode}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def check_python():
    """Check if Python is installed"""
    try:
        version = subprocess.run([sys.executable, "--version"], 
                               capture_output=True, text=True)
        print(f"✅ Python found: {version.stdout.strip()}")
        return True
    except:
        print("❌ Python is not installed or not in PATH")
        return False

def main():
    print("\n" + "="*50)
    print("  UOT Admission Portal - Setup and Launch")
    print("="*50 + "\n")
    
    if not check_python():
        return 1
    
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    print(f"✅ Project root: {project_root}\n")
    
    venv_path = os.path.join(project_root, "venv")
    if not os.path.exists(venv_path):
        print("Creating virtual environment...")
        if not run_command(
            f"{sys.executable} -m venv venv",
            "Virtual Environment Setup"
        ):
            return 1
        print("✅ Virtual environment created")
    else:
        print("✅ Virtual environment already exists")
    
    if platform.system() == "Windows":
        activate_cmd = f"venv\\Scripts\\activate.bat && "
    else:
        activate_cmd = f"source venv/bin/activate && "
    
    check_flask = f"{activate_cmd}python -c \"import flask; print(flask.__version__)\""
    try:
        result = subprocess.run(check_flask, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Flask already installed: {result.stdout.strip()}")
        else:
            raise Exception("Flask not found")
    except:
        print("Installing dependencies...")
        if not run_command(
            f"{activate_cmd}pip install -r requirements.txt",
            "Dependencies Installation"
        ):
            return 1
        print("✅ Dependencies installed")
    
    logs_dir = os.path.join(project_root, "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        print(f"✅ Created logs directory: {logs_dir}")
    
    print("\n" + "="*50)
    print("  Starting Application...")
    print("="*50)
    print("\n✅ Application is starting...\n")
    print("   URL: http://localhost:5000")
    print("   Press Ctrl+C to stop the server\n")
    
    run_cmd = f"{activate_cmd}python main.py"
    os.system(run_cmd)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
