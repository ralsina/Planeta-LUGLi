"""
vellum-templates.py: rawdog plugin to support Vellum's template syntax
Based on templateParser.py from Vellum 1.0a5 (copyright Stuart Langridge, and
under the GNU GPL): http://www.kryogenix.org/code/vellum/
rawdog glue by Adam Sampson <azz@us-lot.org>
"""

import rawdoglib.plugins

import re, sys, traceback
try:
	import cStringIO as StringIO
except:
	import StringIO

class TemplateParser:
	def __init__(self):
		self.reg = re.compile('(<%=|<%|%>)')

	def fill_template(self, data, dict, result):
		fields = self.reg.split(data)
		fields = filter(lambda x: len(x) <> 0, fields)

		in_code = 0
		in_var = 0
		lines = []

		for f in fields:
			if f == '<%':
				in_code = 1
			elif f == '<%=':
				in_var = 1
			elif f == '%>':
				in_code = 0
				in_var = 0
			else:
				if in_code:
					for line in f.split('\n'):
						lines.append(line.strip() + '\n')
				elif in_var:
					lines.append("sys.stdout.write(" + f.strip() + ")\n")
				else:
					lines.append('sys.stdout.write("""' + f.replace('"','\\"') + '""")\n')

		indent = 0
		code = ''
		for line in lines:
			if line.strip() == '':
				continue
			if line.strip() == 'end':
				indent -= 1
				continue
			code += ('\t' * indent) + line + '\n'
			if line.rstrip()[-1] == ':':
				indent += 1

		output = StringIO.StringIO()
		stdout = sys.stdout
		sys.stdout = output
		if "sys" not in dict.keys():
			dict["sys"] = sys
		try:
			exec code in dict
		except:
			print >>sys.stderr, "Python exception while expanding template:"
			traceback.print_exc()
			sys.exit(1)
		sys.stdout = stdout
		result.value = output.getvalue()
		return False

rawdoglib.plugins.attach_hook("fill_template", TemplateParser().fill_template)

