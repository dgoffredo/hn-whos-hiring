set xdata time
set timefmt '%Y-%m'
set format x '%Y-%m'

# month    jobs  ai%  remote%  onsite%  hybrid%  ny%  fulltime%
# -------  ----  ---  -------  -------  -------  ---  ---------
# 2025-08  278   50   54       38       20       13   55       
# 2025-07  325   50   54       38       21       15   56       
# 2025-06  349   46   52       38       19       17   58
# ...

set title "HN Who's Hiring Statistics"
set xlabel 'Month'
set ylabel 'Percentage of Job Postings Having Property'
set y2label 'Number of Job Postings'

set y2tics

set terminal svg size 1920,1080 fixed enhanced font 'Arial,20' butt dashlength 1.0 background rgb 'white'
set output 'stats.svg'

plot 'stats.tab' using 1:2 title 'Total Postings [right axis]' axes x1y2 pointtype 7, \
     '' using 1:3 title 'AI% [left axis]' axes x1y1 pointtype 2, \
     '' using 1:4 title 'Remote% [left axis]' axes x1y1 pointtype 3, \
     '' using 1:5 title 'Onsite% [left axis]' axes x1y1 pointtype 4, \
     '' using 1:6 title 'Hybrid% [left axis]' axes x1y1 pointtype 5, \
     '' using 1:7 title 'NY% [left axis]' axes x1y1 pointtype 6, \
     '' using 1:8 title 'Fulltime% [left axis]' axes x1y1 pointtype 1

