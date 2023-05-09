regex_pattern = r"\D+"	#non-decimal digit
import re
print("\n".join(re.split(regex_pattern, input())))
