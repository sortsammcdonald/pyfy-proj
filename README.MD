# PyFy project

## 2025.10.18

Not sure how much further I can go with this project as it is. Maybe using the new data set will help. For this though I will have to think of some other ways to structure the data. Some ideas include:

- Replicating the daily spending tracking, but over a finite time.
- Grouping data by category / type 
- Reviewing changes in average spend 

After this I can start to think about visualisations 

## Next steps

- Play around with Credit3.csv, transform the data
- Note some simple commands to build scripts form 

## Potential activities

- Review Python automation book again 
- Review [Matplotlib examples](https://matplotlib.org/stable/gallery/index.html) 

Trying out codex from OpenAI, let's see if this helps.

## 2025.10.14

Let's see if I can put the plotting functions in a seperate file and call from there.

I'm not sure there is a way to remove the hardcoding from main.py, the problem is that the columns required are so specific, that a function would not be generic enough in any case.

Perhaps the best thing is to do a deeper dive into matplotlib and see if there are any other interesting visualisations I could create...

## 2025.10.11

Was able to reimplement combinig the files in main. However I'm still not happy about hardcoding variables there, it should be possible to specify the relevant rows at runtime.

Similarly, I think it would be better to define the plotting execution in a seperate file.

## 2025.10.04

## Next stpes

- Complete the original programme
-- Implement combine files in Main: 
-- Combine files requires list of dfs to combine as well as common columns and an index
-- How do I tell the programme to expect those in main?

Let's finish off this project and start a more advanced version.

- Implement combined 

## 2024.08.17

This is part of an ongoing effort to review my personal finances with Python scripts. The code and samples here are purely for demonstration.

Currently, this version of the project, features two CSV files representing credit card statements. The programme combines the files into a single Data Frame, and from there generates a Matplotlib chart showing daily spending.
