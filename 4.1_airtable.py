from airtable import airtable
at = airtable.Airtable('appuD7yMcoCuA0bOB', 'keyfm7L1butbMDXeC')

# Get a single record
record = at.get('IBKR-Algo-Webhooks')
print(record)

# Iterate over records
for record in at.iterate('IBKR-Algo-Webhooks', batch_size=0, filter_by_formula=None, view=None, max_records=1, fields=[]):
    print(record)





