import sys
import re

pattern = "^RUN \d{6} COMPLETED\. OUTPUT IN FILE [a-z]+\.dat\.$"
regexp = re.compile(pattern)

for line in sys.stdin:
    result = regexp.search(line)

    if result:
        sys.stdout.write(line)