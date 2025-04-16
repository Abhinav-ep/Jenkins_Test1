import difflib
import sys
import re

TEMPLATE_FILE = 'templates/template1.sh'
SCRIPT_FILE = 'scripts/script1.sh'

# Define a function to clean lines (strip empty lines, remove comments, and replace placeholders)
def clean_lines(lines, is_template=False):
    cleaned_lines = []
    for line in lines:
        line = line.strip()

        # Ignore empty lines and comments
        if line and not line.startswith('#'):
            if is_template:
                # Replace placeholders in template with a common placeholder
                line = re.sub(r'<NUM\d+>', '<NUM>', line)  # Replace all placeholders like <NUM1>, <NUM2>, etc.
            else:
                # Replace actual values in script with the common placeholder
                line = re.sub(r'num\d+\s*=\s*\d+', 'num<NUM> = <NUM>', line)  # Replace concrete numbers

            cleaned_lines.append(line)

    return cleaned_lines

# Read and clean the template or script file
def read_clean(path, is_template=False):
    with open(path, 'r') as f:
        return clean_lines(f.readlines(), is_template)

def main():
    template = read_clean(TEMPLATE_FILE, is_template=True)  # True for template
    script = read_clean(SCRIPT_FILE, is_template=False)    # False for script

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


