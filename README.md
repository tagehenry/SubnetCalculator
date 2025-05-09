# SubnetCalculator

## Overview
The Subnet Calculator is a Flask-based web application that allows users to calculate subnet information for a given IP address and subnet mask. It provides details such as the network address, broadcast address, usable host range, and total usable hosts.

## Features
- Input IP address and subnet mask in CIDR or dotted-decimal format.
- Calculate and display:
  - Subnet Mask
  - Network Address
  - Broadcast Address
  - Usable Host Range
  - Total Usable Hosts

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd SubnetCalculator
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open a web browser and navigate to `http://127.0.0.1:5000`.
3. Enter the IP address and subnet mask in the form and submit to view the results.
