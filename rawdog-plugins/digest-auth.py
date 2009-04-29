"""
rawdog plugin to add support for digest authentication.
Adam Sampson <ats@offog.org>

This is compatible with rawdog's normal basic authentication support, using
the existing "user" and "password" feed arguments.
"""

import rawdoglib.plugins
import urllib2

def add_handlers(rawdog, config, feed, handlers):
	class DummyPasswordMgr:
		def __init__(self, creds):
			self.creds = creds
		def add_password(self, realm, uri, user, passwd):
			pass
		def find_user_password(self, realm, authuri):
			return self.creds

	if feed.args.has_key("user") and feed.args.has_key("password"):
		mgr = DummyPasswordMgr((feed.args["user"], feed.args["password"]))
		handlers.append(urllib2.HTTPDigestAuthHandler(mgr))

rawdoglib.plugins.attach_hook("add_urllib2_handlers", add_handlers)

