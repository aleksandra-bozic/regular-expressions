import sys
import re

pattern = "Fred"
regexp = re.compile(pattern, re.IGNORECASE)

for line in sys.stdin:
    result = regexp.search(line)

    if result:
        sys.stdout.write(line)