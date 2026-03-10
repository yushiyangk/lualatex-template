import platform
import unicodedata
import sys

from collections import deque, OrderedDict
from datetime import datetime

uppercase: deque[int] = deque()
titlecase: OrderedDict[int, list[int]] = OrderedDict()
letters: deque[int] = deque()

for i in range(sys.maxunicode):
	unicode_char = chr(i)
	cat = unicodedata.category(unicode_char)
	if cat == 'Lu':
		uppercase.append(ord(unicode_char))
		letters.append(ord(unicode_char))
	elif cat == 'Lt':
		titlecase[ord(unicode_char)] = list(ord(nfkc_char) for nfkc_char in unicodedata.normalize('NFKC', unicode_char))
		letters.append(ord(unicode_char))
	elif cat in ('Ll', 'Lm', 'Lo'):
		letters.append(ord(unicode_char))

comment = f"Unicode data generated from Python {platform.python_version()} (using Unicode {unicodedata.unidata_version}) at {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC%z')}"
lua_comment = f"-- {comment}"

lua_uppercase = r"UNICODE_UPPERCASE_SET={[" + r"]=1,[".join(str(n) for n in uppercase) + r"]=1}"

lua_titlecase_entries = []
for composite_n, decomposition in titlecase.items():
	lua_titlecase_entries.append(r"[" + str(composite_n) + r"]={" + ','.join(str(decomp_n) for decomp_n in decomposition) + r"}")
lua_titlecase = r"UNICODE_TITLECASE_DECOMPOSITION={" + r",".join(lua_titlecase_entries) + r"}"

lua_letter_ranges = []
current_range = None
for letter_n in letters:
	if current_range is None:
		current_range = [letter_n, letter_n]
	elif letter_n == current_range[1] + 1:
		current_range[1] = letter_n
	else:
		lua_letter_ranges.append(current_range)
		current_range = [letter_n, letter_n]

lua_letter_ranges = r"UNICODE_SORTED_LETTER_RANGES={" + r",".join(r"{" + str(start_n) + r"," + str(end_n) + r"}" for start_n, end_n in lua_letter_ranges) + r"}"

lua_out = f"{lua_comment}\n{lua_uppercase}\n{lua_titlecase}\n{lua_letter_ranges}"

print(comment)

fout_name = "casemap.lua"
with open(fout_name, 'w', encoding='utf-8') as fout:
	fout.write(lua_out)
	print(f"Wrote {len(lua_out)} characters ({len(lua_out.encode('utf-8'))} bytes) to {fout_name}")
