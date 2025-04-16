import difflib
import sys
import re

TEMPLATE_FILE = 'templates/template1.sh'
SCRIPT_FILE = 'scripts/script1.sh'

# Define a function to clean lines (strip empty lines, remove comments, and replace placeholders)
def clean_lines(lines):
    cleaned_lines = []
    for line in lines:
        line = line.strip()

        # Ignore empty lines and comments
        if line and not line.startswith('#'):
            # Replace placeholders with a common placeholder (like <NUM>)
            line = re.sub(r'<NUM\d+>', '<NUM>', line)
            cleaned_lines.append(line)

    return cleaned_lines

# Read and clean the template or script file
def read_clean(path):
    with open(path, 'r') as f:
        return clean_lines(f.readlines())

def main():
    template = read_clean(TEMPLATE_FILE)
    script = read_clean(SCRIPT_FILE)

    # Compare the cleaned template and script using unified diff
    diff = list(difflib.unified_diff(
        template, script, fromfile='template', tofile='script', lineterm=''
    ))

    if diff:
        print("❌ Script does not match template:")
        print('\n'.join(diff))
        sys.exit(1)
    else:
        print("✅ Script matches the template.")

if __name__ == '__main__':
    main()

