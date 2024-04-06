# FTDS-week1-test

## Problem 1

There are two types of text files in the data folder.\
Create a function that has a filepath as input.\
There are two possible files as input:

- A text file of only numbers (185761728456179235)

- A text file of a story(Once upon a time, there was a...)

If the file contains only numbers, return the first 10 characters.

But if the file contains a story, return a modified string that’s all lowercase. Remember to strip the `\n` from the file contents.<br/>
Also return a list of the top 5 most frequent words in the file. <br/>

The return statement should be in the format below: <br/>
`return 'yourmodifiedstring', [a,b,c,d,e]`

where `'yourmodifiedstring'` is the modified string that's all lowercase and `[a,b,c,d,e]` is the list of the top 5 most frequent words in the file.

Please check the data folder for the sample data files.
