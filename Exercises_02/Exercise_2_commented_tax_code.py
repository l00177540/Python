# Tax calc program with comments

income = 123456
single_person_tax_alowance = 36000
# Tax_allowance as it was pre Budget 2023
taxable_at_20_percent = income-single_person_tax_alowance
taxable_at_40_percent = income-taxable_at_20_percent
percent_tax_20 = taxable_at_20_percent * .2
percent_tax_40 = taxable_at_40_percent * .4
total_tax = percent_tax_20 + percent_tax_40
print (total_tax)
"""
This code was created in August 2022
It will need to be updated in light of the Irish Budget announcement in September 2022
to reflect the new tax allowances
"""
