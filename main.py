import os
import json
import requests
import tornado.web
import tornado.ioloop
import tornado.autoreload

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

class landingPage(tornado.web.RequestHandler):
    def get(self):
        self.render("indexx.html")
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", landingPage),
        (r"/register", basicRequestHandler),
        (r"/regrequ", regRequ),
        (r"/deregister", basicDeRequestHandler),
        (r"/deregrequ", deRegRequ),
        (r"/paymentauth", basicPayHandler),
        (r"/payrequ", payRequ),
        (r"/paymentrevauth", basicRevHandler),
        (r"/revRequ", revRequ),
    ])

    app.listen(port)
    # TODO remove in prod
    tornado.autoreload.start()
    print("I'm listening on port specified")
    tornado.ioloop.IOLoop.current().start()
