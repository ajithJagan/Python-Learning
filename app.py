from flask import Flask
import logging

app = Flask(__name__)

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Use path variable
@app.route('/name/<name>', methods=["GET"])
def home(name):
    logger.info(f"Accessed /name with name: {name}")
    return f"My name is {name}"

if __name__ == "__main__":
    logger.info("Starting Flask app")
    app.run(host='0.0.0.0', port=5000)
