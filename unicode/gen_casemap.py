import platform
import unicodedata
import sys

from collections import deque, OrderedDict
from datetime import datetime

uppercase: deque[int] = deque()
titlecase: OrderedDict[int, list[int]] = OrderedDict()

for i in range(sys.maxunicode):
	unicode_char = chr(i)
	cat = unicodedata.category(unicode_char)
	if cat == 'Lu':
		uppercase.append(ord(unicode_char))
	elif cat == 'Lt':
		titlecase[ord(unicode_char)] = list(ord(nfkc_char) for nfkc_char in unicodedata.normalize('NFKC', unicode_char))

comment = f"Unicode data generated from Python {platform.python_version()} (using Unicode {unicodedata.unidata_version}) at {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC%z')}"
lua_comment = f"-- {comment}"
lua_uppercase = 'unicode_uc={[' + ']=1,['.join(str(n) for n in uppercase) + ']=1}'
lua_titlecase_entries = []
for composite_n, decomposition in titlecase.items():
	lua_titlecase_entries.append('[' + str(composite_n) + ']={' + ','.join(str(decomp_n) for decomp_n in decomposition) + '}')
lua_titlecase = 'unicode_tc={' + ','.join(lua_titlecase_entries) + '}'
lua_out = f"{lua_comment}\n{lua_uppercase}\n{lua_titlecase}"

print(comment)

fout_name = "casemap.lua"
with open(fout_name, 'w', encoding='utf-8') as fout:
	fout.write(lua_out)
	print(f"Wrote {len(lua_out)} characters ({len(lua_out.encode('utf-8'))} bytes) to {fout_name}")
