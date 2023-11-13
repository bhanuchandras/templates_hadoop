import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Data for the graph
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

# HTML content for the graph
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Simple HTML Graph</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>

<div id="graph"></div>

<script>
    // Data for the graph
    var x_data = {x_data};
    var y_data = {y_data};

    // Create a trace
    var trace = {{
        x: x_data,
        y: y_data,
        type: 'scatter'
    }};

    // Create a layout
    var layout = {{
        title: 'Simple HTML Graph',
        xaxis: {{
            title: 'X-Axis'
        }},
        yaxis: {{
            title: 'Y-Axis'
        }}
    }};

    // Plot the graph
    Plotly.newPlot('graph', [trace], layout);
</script>

</body>
</html>
"""

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@outlook.com'
subject = 'HTML Graph Email'

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the HTML content
html_part = MIMEText(html_content, 'html')
message.attach(html_part)

# Connect to the SMTP server and send the email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_email_password'

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Email sent successfully.')
