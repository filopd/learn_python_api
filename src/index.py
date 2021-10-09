# Import Tornado Packages
import tornado.web # This is used to create API Handlers
import tornado.ioloop # This is used to keep the program running on the server continuously.


# Create Handler Class inhertiting Tornado RequestHandler module.
class basicRequestHandler(tornado.web.RequestHandler):
    # Create a GET method.
    def get(self):
        # Print the details when GET executed.
        self.write("This is a Get Method Result from Server.")


# Create main method which should be the only one.
if __name__ == "__main__":
    # Create an Application with handler URL mapping as a Tuple.
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])
    # Select a Port
    port = 8082
    # Tell Application to listen this port.
    app.listen(port=port)
    print(f"API Application is listening on PORT {port}...")
    # Now start the looping so that this app will keep listening using current thread start.
    tornado.ioloop.IOLoop.current().start()

