# Variables
presidental_turnout = 16
senate_turnout = 26
census_response_rate = 100
sub_size = 3741

# Cube root function since python's math module doesn't include one
def get_cube_root(num):
    return num ** (1. / 3)

# The equation. This can be found in Appendix 1.3 of the SimDemocracy Constitution: https://docs.google.com/document/d/1x3EwwglsRgnBRDhJOB8DcSZHG7ZLahG_enitXqqvDWA/edit#heading=h.jj8r0y1g96nf
equation =  round(1.25 * (get_cube_root(2 * presidental_turnout + senate_turnout + census_response_rate + 0.1 * sub_size)), 0)

# Now show the equation
print(equation)