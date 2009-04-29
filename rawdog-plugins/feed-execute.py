# Add a feed option to execute a command before or after updating the feed.
# This is useful if, for example, you have a file: feed that's generated on the
# fly by a screen-scraping program.
# Usage example:
# feed 3h file:/tmp/scraped.rss
#     pre-execute scrape http://somewhere/ >/tmp/scraped.rss
#     post-execute rm /tmp/scraped.rss

import rawdoglib.plugins, os

def pre_update_feed(rawdog, config, feed):
	if feed.args.has_key("pre-execute"):
		os.system(feed.args["pre-execute"])
	return True
rawdoglib.plugins.attach_hook("pre_update_feed", pre_update_feed)

def post_update_feed(rawdog, config, feed, seen):
	if feed.args.has_key("post-execute"):
		os.system(feed.args["post-execute"])
	return True
rawdoglib.plugins.attach_hook("post_update_feed", post_update_feed)
