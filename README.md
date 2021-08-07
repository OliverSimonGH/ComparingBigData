# Comparing Big Data

This was coded to be educational for me.

Wrote a small programme that compares 80,000 emails from a text file against a CSV file that contains 40GB of data.
The programme will compare all 80,000 emails for each line in the CSV file, making the computation time costly without proper techniques.

At the start of the programme, the 80,00 emails are laoded into a BST that gets balanced to improve saerch times. This BST is small enough to be stored in memory, making this possible. 
Then the CSV is read in chunks of 100,000 and compared against the BST to find data that correlates.

Once the data is found, it will be written to a file to show the results.
This programme had a dramatic increase in performance when comaring a BST to an array.
When using an array, there was an average of about 30 seconds to find a matching line, as it has to read all of the array.
The BST finished in milliseconds when finiding a result due to its data structure and being balanced.
