import json
import falcon
import MeCab

class MecabResource(object):
  def on_post(self, req, resp):
    body = req.stream.read().decode('utf-8')
    tagger = MeCab.Tagger()
    resp.body = tagger.parse(body)

app = falcon.API()
app.add_route("/", MecabResource())

if __name__ == "__main__":
  from wsgiref import simple_server
  httpd = simple_server.make_server('', 8000, app)
  httpd.serve_forever()
