#/bin/python

import urllib.request
import json
import os
import re

TOKEN = os.environ['CR_TOKEN']

for f in os.listdir("posts"):
	content = open(os.path.join("posts", f), "r").read()
	match = re.search('cr_group_id: ?([\d]*)', content, re.MULTILINE)
	if not match:
		continue

	group_id = match.group(1)

	print(group_id)

	req = urllib.request.urlopen("https://rest.cleverreach.com/v2/groups.json/{group}/stats?token={token}".format(token=TOKEN, group=group_id))
	data = json.loads(req.read().decode('utf8'))

	print(data)

	count = data['active_count']

	total = 20000
	if count > 100000:
		total = 200000
	elif count > 750000:
		total = 100000
	elif count > 50000:
		total = 75000
	elif count > 30000:
		total = 50000
	elif count > 20000:
		total = 30000

	percent = total / count * 100

	replaced = []

	for line in content.splitlines():
		if line.startswith("currently:"):
			replaced.append("currently: {}".format(count))
		elif line.startswith("total:"):
			replaced.append("total: {}".format(total))
		elif line.startswith("percent:"):
			replaced.append("percent: {}".format(percent))
		else:
			replaced.append(line)

	with open(os.path.join("posts", f), "w") as writer:
		writer.write("\n".join(replaced))