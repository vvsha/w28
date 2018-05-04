
"""
The widget passes the test ie its presence is verified.
Not a particularly good test tho'...
"""
#from nose.tools import raises
from tw2.jqplugins.fancytree import FancyTreeWidget
from tw2.core.testbase import WidgetTest


class TestFancyTreeWidget(WidgetTest):

    engines = ['mako']

    widget = FancyTreeWidget
    attrs = dict(id="test-widget")
    params = {'options': {
        'source': [
            {"title": "Node 1", "key": "1"},
            {"title": "Folder 2", "key": "2", "folder": True,
                "children": [
                    {"title": "Node 2.1", "key": "3"},
                    {"title": "Node 2.2", "key": "4"},
                    {"title": "Node 2.3", "key": "5"}
                ]
             },
        ]
    }}
    expected = """
<div>
    <div id="test-widget"></div>
</div>
"""
