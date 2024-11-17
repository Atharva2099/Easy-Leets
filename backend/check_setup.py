

import os
from pathlib import Path

def main():
    print("MAAI Backend Setup Check")
    print("=" * 50)
    
    # Check current directory
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Check if we're in the backend directory
    if not current_dir.name == 'backend':
        print("❌ Please run this script from the backend directory")
        return
    
    # Check for .env file
    env_file = current_dir / '.env'
    if not env_file.exists():
        print("❌ .env file not found")
        print("Creating .env file template...")
        with open(env_file, 'w') as f:
            f.write("SAMBANOVA_API_KEY=your_sambanova_key_here\n")
            f.write("NUGEN_API_KEY=your_nugen_key_here\n")
        print("✅ Created .env file template")
    else:
        print("✅ .env file exists")
    
    # Create directory structure
    directories = [
        'app',
        'app/api',
        'app/api/routes',
        'services',
        'utils'
    ]
    
    for dir_path in directories:
        dir_full_path = current_dir / dir_path
        if not dir_full_path.exists():
            dir_full_path.mkdir(parents=True)
            print(f"Created directory: {dir_path}")
        
        # Create __init__.py in each directory
        init_file = dir_full_path / '__init__.py'
        if not init_file.exists():
            init_file.touch()
            print(f"Created {dir_path}/__init__.py")
    
    print("\nDirectory structure setup complete!")
    print("\nNext steps:")
    print("1. Edit .env file and add your API keys")
    print("2. Run: uvicorn app.main:app --reload --log-level debug")

if __name__ == "__main__":
    main()



