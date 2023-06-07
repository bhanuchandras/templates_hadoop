from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  # Get the data from the JavaScript
  data = request.args.get("data")

  # Render the template with the data
  return render_template("index.html", data=data)

if __name__ == "__main__":
  app.run(debug=True)
