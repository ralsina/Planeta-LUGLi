"""
Add the "from the ... dept." lines to the descriptions of Slashdot
articles (found in the feed as slash:department).
"""

class Slashdot:
    html = '%s\n<p style="font-size:x-small">from the %s dept.</p>'
    def output(self, rawdog, config, feed, article, itembits):
        if not article.entry_info.has_key('slash_department'):
            return True

        dept = article.entry_info['slash_department']
        itembits["description"] = self.html % (itembits["description"], dept)
        return True


### Init code
import rawdoglib.plugins
rawdoglib.plugins.attach_hook("output_item_bits", Slashdot().output)
