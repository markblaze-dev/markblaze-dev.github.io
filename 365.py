# Open a new HTML file for writing
with open('output.html', 'w') as file:
    # Write the HTML header
    file.write('<html>\n<head>\n</head>\n<body>\n<table border="1">\n')

    # Loop to replicate the table row 365 times
    for day in range(1, 366):
        file.write(f'  <tr>\n')
        file.write(f'    <td>{day}</td>\n')
        file.write(f'    <td>Placeholder</td>\n')
        file.write(f'    <td>Placeholder</td>\n')
        file.write(f'    <td>Placeholder</td>\n')
        file.write(f'    <td>Placeholder</td>\n')
        file.write(f'    <td>Placeholder</td>\n')
        file.write(f'  </tr>\n')

    # Write the HTML footer
    file.write('</table>\n</body>\n</html>')
