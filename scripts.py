import sys
import subprocess
import shutil
import os
import yaml


def download_python_template():
    """
    Download the Python client library template from the OpenAPI Generator.
    """
    try:
        subprocess.run([
            "openapi-generator-cli",
            "author",
            "template",
            "-g",
            "python",
            "--library",
            "urllib3",
        ])
    except Exception as e:
        print("Exception when generating package: %s\n" % e)


def generate_package():
    """
    Generate the Python client library package using the OpenAPI Generator.
    """
    try:
        subprocess.run([
            "openapi-generator-cli",
            "generate",
            "-g",
            "python",
            "--library",
            "urllib3",
            "-t",
            "lib_template",
            "-o",
            "src",
            "-i",
            "openapi_filtered.yaml",
            "-c",
            "config.json"
        ])
    except Exception as e:
        print("Exception when generating package: %s\n" % e)


def build_distro_package():
    """
    Build the distribution package for the Notehub Py client library.
    """
    try:
        os.chdir("src/")
        # Check if the 'dist/' folder exists
        if os.path.exists("dist"):
            # If it exists, delete it and its contents
            shutil.rmtree("dist")

        # Upgrade the 'build' module
        subprocess.run([
            "python3",
            "-m",
            "pip",
            "install",
            "--upgrade",
            "build"
        ])

        # Generate a new 'dist/' folder  
        subprocess.run([
            "python3",
            "-m",
            "build"
        ])  
    except Exception as e:
        print("Exception when building distro package: %s\n" % e)     


def remove_deprecated_parameters(input_file: str, output_file: str):
    """
    Load an OpenAPI YAML file, remove deprecated parameters, and save to a new file.
    """
    with open(input_file, 'r') as f:
        openapi_spec = yaml.safe_load(f)

    # Traverse paths and operations to remove deprecated parameters
    for path, methods in openapi_spec.get('paths', {}).items():
        for method, operation in methods.items():
            if isinstance(operation, dict):
                # Remove deprecated parameters
                if 'parameters' in operation:
                    operation['parameters'] = [
                        param for param in operation['parameters']
                        if not param.get('deprecated', False)
                    ]
                
                # Remove deprecated requestBody properties if applicable
                if 'requestBody' in operation:
                    content = operation['requestBody'].get('content', {})
                    for content_type, schema in content.items():
                        properties = schema.get('schema', {}).get(
                            'properties', {}
                        )
                        schema['schema']['properties'] = {
                            k: v for k, v in properties.items() 
                            if not v.get('deprecated', False)
                        }

    # Save the modified spec to a new file
    with open(output_file, 'w') as f:
        yaml.dump(openapi_spec, f, sort_keys=False)

    print(f"Filtered OpenAPI spec saved to: {output_file}")

def run_prettier_on_docs():
    """
    Run Prettier on the generated markdown documentation files in the src/docs/ directory.
    This requires Prettier to be installed on the system.
    """
    try:
        docs_dir = "src/docs"
        
        # Check if the docs directory exists
        if not os.path.exists(docs_dir):
            print(f"Documentation directory {docs_dir} not found. Skipping Prettier formatting.")
            return
            
        print(f"Running Prettier on markdown documentation in {docs_dir}...")
        
        # Check if Prettier is installed
        result = subprocess.run(
            ["npx", "--no-install", "prettier", "--version"], 
            capture_output=True, 
            text=True
        )
        
        if result.returncode != 0:
            print("Prettier not found. Installing Prettier...")
            subprocess.run(["npm", "install", "--global", "prettier"])
        
        # Run Prettier on all markdown files in the src/docs/ directory and subdirectories
        subprocess.run([
            "npx", 
            "prettier", 
            "--write", 
            f"{docs_dir}/**/*.md"
        ])
        print("Prettier formatting of documentation completed successfully.")
    except Exception as e:
        print(f"Exception when running Prettier on docs: {e}")

def run_black_on_python():
    """
    Run Black formatter on all Python files in the src/ directory.
    This requires Black to be installed on the system.
    Uses python -m black to ensure we use the installed package.
    """
    try:
        src_dir = "src"
        
        # Check if the src directory exists
        if not os.path.exists(src_dir):
            print(f"Source directory {src_dir} not found. Skipping Black formatting.")
            return
            
        print(f"Running Black on Python files in {src_dir}...")
        
        # Install Black if needed (will be a no-op if already installed)
        print("Ensuring Black is installed...")
        subprocess.run([
            "python3", 
            "-m", 
            "pip", 
            "install", 
            "black"
        ])
        
        # Run Black using Python module approach to avoid path issues
        subprocess.run([
            "python3",
            "-m",
            "black", 
            src_dir
        ])
        print("Black formatting of Python files completed successfully.")
    except Exception as e:
        print(f"Exception when running Black on Python files: {e}")
    
def format_code():
    """
    Format both Python and Markdown files in the repository.
    """
    run_black_on_python()
    run_prettier_on_docs()
    print("All code formatting completed.")        

def generate_and_format():
    """
    Convenience function to generate the package and run Prettier on it.
    """
    remove_deprecated_parameters("openapi.yaml", "openapi_filtered.yaml")
    generate_package()
    format_code()
    build_distro_package()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: python3 scripts.py [download_python_template | " 
            "generate_package | build_distro_package | "
            "remove_deprecated_parameters | run_prettier_on_docs | "
            "run_black_on_python | format_code | generate_and_format]"
        )
        sys.exit(1)
    
    script_to_run = sys.argv[1]
    if script_to_run == "download_python_template":
        download_python_template()
    elif script_to_run == "generate_package":
        generate_package()
    elif script_to_run == "build_distro_package":
        build_distro_package()
    elif script_to_run == "remove_deprecated_parameters":
        remove_deprecated_parameters("openapi.yaml", "openapi_filtered.yaml")
    elif script_to_run == "run_prettier_on_docs":
        run_prettier_on_docs()
    elif script_to_run == "run_black_on_python":
        run_black_on_python()
    elif script_to_run == "format_code":
        format_code()    
    elif script_to_run == "generate_and_format":
        generate_and_format()
    else:
        print(
            "Invalid script name. Use one of: download_python_template, "
            "generate_package, build_distro_package, "
            "remove_deprecated_parameters, run_prettier_on_docs, "
            "run_black_on_python, format_code, generate_and_format"
        )
        sys.exit(1)