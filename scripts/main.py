import gml
import sys
import os

if len(sys.argv) != 3:
    print("Usage: <script> file.gml outputDir")

# create a parser, load a file, and parse it!
parser = gml.Parser()
parser.load_gml(sys.argv[1])
parser.parse()

graph = parser.graph

files = {}

n = {}
for nodeID in graph.graph_nodes:
    node = graph.graph_nodes[nodeID]
    n = node
    files[node.label] = []

for edge in graph.graph_edges:
    source = edge.source_node
    target = edge.target_node
    files[source.label].append(target.label)

outputDir = sys.argv[2]
os.makedirs(outputDir, exist_ok=True)

for label in files:
    fn = label + ".md"
    fullPath = os.path.join(outputDir, fn)
    with open(fullPath, 'w') as f:
        contents = '# '  + label + "\n\n"

        for t in files[label]:
            contents += "- [[" + t + "]]\n"

        f.write(contents)