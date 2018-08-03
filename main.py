import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        location =self.request.get("location")
        template = env.get_template("templates/hello.html")
        templateVars = {
            "name" : name,
            "location" : location,
        }
        self.response.write(template.render(templateVars))


class SecretEntrance(webapp2.RequestHandler):
    def get(self):
        self.response.write("Shhh, this is a secret!")

class Goodbye(webapp2.RequestHandler):
    def get(self):
        self.response.write("Than you for visiting our page. Goobye!")

class About(webapp2.RequestHandler):
    def get(self):
        self.response.write("About")
        template = env.get_template("templates/profile.html")
        self.response.write(template.render())

class Photo(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/students.html")
        self.response.write(template.render())

class Students(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/students.html")
        templateVars = {
            "location" : "MTV",
            "students" : ["Kidus", "Leo", "Phoebe", "Jenny", "Lily", "Elvin"]
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/secret", SecretEntrance),
    ("/goodbye", Goodbye),
    ("/about", About),
    ("/photos", Photo),
    ("/students", Students)
], debug=True)









# How to link multiple files of different languages to main python files

#1 Import jinja in app.yaml
#2 import jinja + os to main.y
#3 setup jinja env
#4 get the template from the env
#5 render the template
