import rawdoglib.plugins

def backwards(rawdog, config, articles):
	articles.sort()
	articles.reverse()
	return False

rawdoglib.plugins.attach_hook("output_sort_articles", backwards)
