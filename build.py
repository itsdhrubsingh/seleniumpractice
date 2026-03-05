import json
import os
import shutil

# Read config
with open("config.json", "r", encoding="utf-8") as f:
    configs = json.load(f)

# Read template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Generate files
for env, values in configs.items():
    # Create the environment directory
    os.makedirs(env, exist_ok=True)
    
    # Replace placeholders
    content = template
    for key, value in values.items():
        placeholder = f"{{{{ {key} }}}}"
        content = content.replace(placeholder, value)
    
    # Write the new index.html
    with open(f"{env}/index.html", "w", encoding="utf-8") as f:
        f.write(content)
        
    # Copy style.css to the created directory
    shutil.copy("style.css", f"{env}/style.css")
    
    print(f"Generated {env}/index.html")

print("Build complete!")
