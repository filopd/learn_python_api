# Import Tornado Packages
import re
import tornado.web # This is used to create API Handlers
import tornado.ioloop # This is used to keep the program running on the server continuously.
import os # To check file and dir
import json # To convert data into Json

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

# Create Handler Class inhertiting Tornado RequestHandler module.
class learnResourceParamRequestHandler(tornado.web.RequestHandler):
    # Create a GET method.
    def get(self, studentName, courseId):
        # Print the details when GET executed.
        self.write(f"{studentName} is learning course with id {courseId}.")

# Create Handler Class inhertiting Tornado RequestHandler module.
class jsonReturnRequestHandler(tornado.web.RequestHandler):
    # Create a GET method.
    def get(self):
        d_file = "E:\\Coder\\Python\\Projects\\devl\\learn_python_api\\src\\data.txt"
        # First verify the file.
        if os.path.isfile(d_file):
            res = ""
            # Read the content from file
            with open(d_file, "r") as read_file:
                res = str(read_file.read()).strip()
                res = res.splitlines()
            # Covert it to Json Array
            if len(res) != 0:
                res = json.dumps(res)
                self.write(res)
            else:
                self.write(f"Error: File '{d_file}' is empty.")
        else:
            self.write(f"Error: '{d_file}' File not found.")



# Create main method which should be the only one.
if __name__ == "__main__":
    # Create an Application with handler URL mapping as a Tuple.
    app = tornado.web.Application([
        (r"/", basicRequestHandler), # http://localhost:8082/
        (r"/index", htmlListRequestHandler), # http://localhost:8082/index
        (r"/iseven", isevenQueryParamRequestHandler), # http://localhost:8082/iseven?number=1
        (r"/learning/([A-z]+)/([0-9]+)", learnResourceParamRequestHandler), # http://localhost:8082/learning/Filo/101
        (r"/jsondata", jsonReturnRequestHandler) # http://localhost:8082/jsondata
    ])
    # Select a Port
    port = 8082
    # Tell Application to listen this port.
    app.listen(port=port)
    print(f"API Application is listening on PORT {port}...")
    # Now start the looping so that this app will keep listening using current thread start.
    tornado.ioloop.IOLoop.current().start()


