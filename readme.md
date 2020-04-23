<b>Title: </b>  "MOJ Tech Challenge - Store Application" 
<br>
<b>Author:</b>  Josh Stancombe 
<br>
<b>Last Updated:</b>  15/04/2020 
<br>


## General Notes:
- You will need to run this application in a Python 3 compiler / IDE.

## Description:
- This application acts as a store, and enables users to 'scan' available products to their shopping cart and then checkout. Any number of products can be added (in any order), the user simply has to type the name or code of the product they want to add at the prompt.  

- Once the user is ready to checkout, they can type 'checkout', and their total owed amount will be calculated, along with any current promotional offers. After checkout, the program will be terminated. Additionally, at any point the customer can also see their current cart by typing 'cart', and see a list of products available by typing 'products'. 
  
## How to Run:
- The code can be copied and pasted into any Python compiler or IDE (see https://repl.it/languages/python3 for a free online IDE). The application is designed to automatically terminate after the checkout has been run. If at any point a user wants to exit the application, they can type 'exit'.
	
## Notes to solving the challenge: 
- I decided to code this challenge in Python, simply as I've previously completed two smaller home projects in Python and enjoyed working with the language (being familiar with some bespoke 'back end' programming). As a further challenge, I'm also looking to re-write this code with JavasScript, HTML & CSS to give it a GUI and grow my skills with front end development. 
	
- The code has been designed to be flexible, human-readable, and easy to follow. For exmaple, changing the product values (code / name / price) only needs to be done once in the product array table, all sections are in a logical order, and the functions are numbered and labelled. 
	
- To the best of my ability, I tried to follow core programming principals (e.g. DRY / KISS), however am aware that this code could be optimized further, given more experience and time with the language. 

## Tests:
- See attached 'Application Testing' document.


## Known 'Tradeoffs' & Change Requests:
- 1. There is currently no option to delete a product from the store
- 2. Float numbers with '.00' are only displaying with 1 decimal place. I have tried to fix this within a reasonable timeframe, however have accepted that this should still be OK to get the product to MVP.


## References of help needed:
- 1. Stack Overflow (https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item) -- I needed to know how to count the occurences of an item in the cart array. This identified the [array].count() method. This can be seen in the 'cartItems' function to count the number of each product currently in the cart.
		
- 2. W3Resource (https://www.w3resource.com/python/built-in-function/int.php) -- I needed to know how to convert a specified value into an integer. I was trying to figure out how best to calculate the BOGOF offer for promo 1. When researching, I discovered that if a float number is divided by two and returned as an 'int()', an 'odd' number would always round down it's '.5' to the nearest integer. This helped me calculate the total amount needed for the BOGOF offer. This can be seen in the 'promotions' function.
		
- 3. Stack Overflow (https://stackoverflow.com/questions/5676646/how-can-i-fill-out-a-python-string-with-spaces) && W3Schools (https://www.w3schools.com/python/ref_string_ljust.asp) -- I needed to know how to fill the space in a string with whitespace. These articles identified the 'ljust()' method which is used for filling a string with whitespace. This can be seen in the 'init', 'products' and 'checkout' functions when using 'print()' to somewhat visualise a table.

- 4. Stack Overflow (https://stackoverflow.com/questions/1317558/converting-a-float-to-a-string-without-rounding-it/1317578) -- I needed to know how to convert a float to a string without rounding it in order to use the 'ljust' method noted above. This confirmed that putting what i needed into 'str()' would allow me to use the 'ljust' method. This can be seen in the 'init' and 'checkout' functions.
		
- 5. YouTube (https://www.youtube.com/watch?v=LaCjP0uQxzc) -- I needed some clarification on how to pass variables between functions. This identified how to return a value from a function.
