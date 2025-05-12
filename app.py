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

@app.route('/compare', methods=['POST'])
def compare():
    ip1 = request.form.get('ip1')
    subnet1 = request.form.get('subnet1')
    ip2 = request.form.get('ip2')
    subnet2 = request.form.get('subnet2')

    # Use the new feature to check if the IPs are in the same range
    reachable = calculatesubnet.are_ips_in_same_range(ip1, subnet1, ip2, subnet2)

    # Render a new results page for this feature
    return render_template('compare_result.html', ip1=ip1, subnet1=subnet1, ip2=ip2, subnet2=subnet2, reachable=reachable)

if __name__ == '__main__':
    app.run(debug=True)
