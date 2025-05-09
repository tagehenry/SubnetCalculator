import calculatesubnet
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    ip = request.form.get('ip')
    subnet = request.form.get('subnet')
    return ip, subnet

@app.route('/result', methods=['POST'])
def result():
    ip = request.form.get('ip')
    subnet = request.form.get('subnet')
    # Call the subnet_calculator function with user input
    ip, subnet_bits = calculatesubnet.conver_to_cidr(ip, subnet)
    results = calculatesubnet.subnet_calculator(ip, subnet_bits)
    # Debugging: Log the results dictionary
    print("DEBUG: Subnet Calculation Results:", results)
    # Render the results in a template
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
