from wikiarguments_rest import app

doc = """\
<h2>Wikiarguments-API</h2>
<ul>
    <li>GET all questions: <strong>/questions/</strong>
    <li>GET single question: <strong>/questions/&lt;string:question_url&gt;</strong>
    <li>GET all arguments: <strong>/questions/&lt;string:question_url&gt;/arguments/</strong>
    <li>GET single argument: <strong>/questions/&lt;string:question_url&gt;/arguments/&lt;string:argument_url&gt;</strong>
</ul>

<h3>Options</h3>

<ul>
    <li>details=(0|1): include argument / question detail text, default 0 
</ul>

<h3>Examples</h3>

<ul>
<li><a href="/questions/SAA001/arguments?details=0">/questions/SAA001/arguments?details=0</a>
<li><a href="/questions/SAA001/arguments/teilnahme-wird-erleichtert?details=1">/questions/SAA001/arguments/teilnahme-wird-erleichtert?details=1</a>
</ul>
"""


@app.route("/")
def index():
    return doc
