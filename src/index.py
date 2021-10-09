# Import Tornado Packages
import tornado.web # This is used to create API Handlers
import tornado.ioloop # This is used to keep the program running on the server continuously.


# Create Handler Class inhertiting Tornado RequestHandler module.
class basicRequestHandler(tornado.web.RequestHandler):
    # Create a GET method.
    def get(self):
        # Print the details when GET executed.
        self.write("This is a Get Method Result from Server.")

# Create Handler Class inhertiting Tornado RequestHandler module.
class htmlListRequestHandler(tornado.web.RequestHandler):
    # Create a GET method.
    def get(self):
        # Render index.html page created in the same directory.
        self.render("index.htm")

# Create Handler Class inhertiting Tornado RequestHandler module.
class isevenQueryParamRequestHandler(tornado.web.RequestHandler):
    # Create a GET method.
    def get(self):
        # take the input, verify it and return the result.
        ip_1 = self.get_argument("number")
        if ip_1.isdigit():
            ip_1 = int(ip_1)
            res = "even" if ip_1 % 2 == 0 else "odd"
            self.write(f"Input number {ip_1} is {res}.")
        else:
            self.write(f"Error: {ip_1} is not a number.")



# Create main method which should be the only one.
if __name__ == "__main__":
    # Create an Application with handler URL mapping as a Tuple.
    app = tornado.web.Application([
        (r"/", basicRequestHandler), # http://localhost:8082/
        (r"/index", htmlListRequestHandler), # http://localhost:8082/index
        (r"/iseven", isevenQueryParamRequestHandler) # http://localhost:8082/iseven?number=1
    ])
    # Select a Port
    port = 8082
    # Tell Application to listen this port.
    app.listen(port=port)
    print(f"API Application is listening on PORT {port}...")
    # Now start the looping so that this app will keep listening using current thread start.
    tornado.ioloop.IOLoop.current().start()


