import sys
import re

pattern = "Fred"
regexp = re.compile(pattern) # Case sensitive

for line in sys.stdin:
    result = regexp.search(line)

    if result:
        sys.stdout.write(line)