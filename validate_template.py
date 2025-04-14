import difflib
import sys

TEMPLATE_FILE = 'templates/template1.sh'
SCRIPT_FILE = 'scripts/script1.sh'

def clean_lines(lines):
    return [
        line.strip()
        for line in lines
        if line.strip() and not line.strip().startswith('#')
    ]

def read_clean(path):
    with open(path, 'r') as f:
        return clean_lines(f.readlines())

def main():
    template = read_clean(TEMPLATE_FILE)
    script = read_clean(SCRIPT_FILE)

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
