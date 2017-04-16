import sys
sys.path.insert(0, 'scripts')
from csvDaily import csv_daily
from csvMonthly import csv_monthly

# getting monthly data
csv_monthly()
# getting daily data
csv_daily()
