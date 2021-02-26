# -*- coding: utf-8 -*-
"""
heavily modified from pelican-youtube

"""

from docutils import nodes
from docutils.parsers.rst import directives, Directive

class Collapsible(Directive):

    def boolean(argument):
        """Conversion function for yes/no True/False."""
        value = directives.choice(argument, ("yes", "True", "no", "False"))
        return value in ("yes", "True")

    required_arguments = 0
    optional_arguments = 2
    option_spec = {
        "name" : directives.unchanged,
        "stable" : boolean,
    }

    final_argument_whitespace = True
    has_content = True

    def run(self):

        name = self.options.get("name", None)
        stable = self.options.get("stable", None)
        content = '<br />'.join(self.content)
        section = "{1}_{0}".format(name.replace("/", "_").replace(" ", "_"), "stable" if stable else "dev")
        toggle_block = '<input class="collapsible-toggle" id="{0}" type="checkbox"/>'.format(section)
        label_block = '<label class="collapsible-label" for="{0}">{1}</label>'.format(section, name)


        return [
            nodes.raw("", "<ul>", format="html"),
            nodes.raw("", "<li>", format="html"),
            nodes.raw("", toggle_block, format="html"),
            nodes.raw("", label_block, format="html"),
            nodes.raw("", '<div class="collapsible-content">', format="html"),
            nodes.raw("", '<div class="codeblock">', format="html"),
            nodes.raw("", content, format="html"),
            nodes.raw("", "</div>", format="html"),
            nodes.raw("", "</div>", format="html"),
            nodes.raw("", "</li>", format="html"),
            nodes.raw("", "</ul>\n", format="html"),
        ]

def register():
    directives.register_directive("collapsible", Collapsible)
