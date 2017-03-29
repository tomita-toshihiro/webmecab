import json
import falcon
import MeCab

class MecabResource(object):
  def on_get(self, req, resp):
    msg={"message": "hello, falcon"}
    resp.body = json.dumps(msg)

app = falcon.API()
app.add_route("/", MecabResource())

if __name__ == "__main__":
  from wsgiref import simple_server
  httpd = simple_server.make_server('', 8000, app)
  httpd.serve_forever()
