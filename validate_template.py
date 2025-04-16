import difflib
import sys
import re

TEMPLATE_FILE = 'templates/template3.sh'
SCRIPT_FILE = 'scripts/script3.sh'

def clean_lines(lines, is_template=False):
    cleaned_lines = []
    for line in lines:
        line = line.strip()

        if line and not line.startswith('#'):
            if is_template:
                line = re.sub(r'<NUM\d+>', '<NUM>', line)
            else:
                line = re.sub(r'(\s*=\s*)\d+', r'\1<NUM>', line)

            cleaned_lines.append(line)

    return cleaned_lines

def read_clean(path, is_template=False):
    with open(path, 'r') as f:
        return clean_lines(f.readlines(), is_template)

def main():
    template = read_clean(TEMPLATE_FILE, is_template=True)
    script = read_clean(SCRIPT_FILE, is_template=False)

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
