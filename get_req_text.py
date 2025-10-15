import os
import re
import importlib
import importlib.metadata as metadata

directories = ["Core__", "Improvement__", "Matching__", "Models__", "Utility__"]
extra_files = ["imp.py", "main.py", "call_matching.py"]
output_file = "requirements_generated.txt"

def extract_imports_from_file(file_path):
    imports = set()
    pattern = re.compile(r'^\s*(?:import|from)\s+([\w\.]+)')
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = pattern.match(line)
                if match:
                    module = match.group(1).split('.')[0]
                    imports.add(module)
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")
    return imports

def collect_all_imports(base_path="."):
    all_imports = set()
    for folder in directories:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".py"):
                        all_imports |= extract_imports_from_file(os.path.join(root, file))
    for file in extra_files:
        file_path = os.path.join(base_path, file)
        if os.path.exists(file_path):
            all_imports |= extract_imports_from_file(file_path)
    return all_imports

def get_package_versions(imports):
    versions = {}
    for pkg in sorted(imports):
        try:
            versions[pkg] = metadata.version(pkg)
        except metadata.PackageNotFoundError:
            try:
                mod = importlib.import_module(pkg)
                versions[pkg] = getattr(mod, "__version__", "Not Installed / Built-in")
            except Exception:
                versions[pkg] = "Not Installed / Built-in"
    return versions

def generate_requirements(base_path="."):
    imports = collect_all_imports(base_path)
    versions = get_package_versions(imports)
    with open(output_file, "w", encoding="utf-8") as f:
        for pkg, ver in sorted(versions.items()):
            if ver not in ["Not Installed / Built-in", "N/A"]:
                f.write(f"{pkg}=={ver}\n")
            else:
                f.write(f"# {pkg} ({ver})\n")
    print(f"✅ Requirements list saved to '{output_file}'")

if __name__ == "__main__":
    generate_requirements()
