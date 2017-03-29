import json
import falcon
import MeCab

class MecabResource(object):
  def on_post(self, req, resp):
    body = req.stream.read().decode('utf-8')
    tagger = MeCab.Tagger()

    lines = []
    for line in tagger.parse(body).split("\n"):
      if line == "EOS" or line == "":
        continue

      e = line.split("\t")
      word = e[0]
      results = e[1].split(",")
      lines.append({
        "word": word,
        "results": results
      })

    resp.body = json.dumps(lines)

app = falcon.API()
app.add_route("/", MecabResource())

if __name__ == "__main__":
  from wsgiref import simple_server
  httpd = simple_server.make_server('', 8000, app)
  httpd.serve_forever()
