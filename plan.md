6/26 
set up the dockerfiles and see if anything needs to be moved into a separate microservice

make sure the database is set up correctly

finish planning out the domains for the site 

need to make API views with JSON 

and make sure everything gets installed 

---- objects model/ view/ is adjusted for json. 
---- need to make adjustments for the financial literacy side 
---- likely nee to make a status model for ... ? income type?
----- expenses type ????????

a single account- needs to have the ability to have multiple profiles inside of it- 


income model needs to have a type (passive or active)
dispursement(salary/hourly/fluctuating)
separate compensation(bonus/stocks)
date- paid/plan to paid

expenses(name of the expense/type?/ due date?  )

the goals app needs to be able to poll data from the income app 
a goal can be a net positive goal- (plan trip to italy)
or a net negative goal - (pay off a credit card)
they can be separate based on the profile- 
for the rental property - (i want to save up to buy new appliances within 1 year - estimated cost of appliances / how much i need to put in )
long term goals- (i want to save up for a down payment of a house within 5 years/ i want to save anywhere between 20K and 40K- can show you a midmark average to hit that, some type of sliding scale? )

*look up choices (drop down built into django/ needs to be adjusted ) on the charfield model for expenses and income - 
*decide if these need to be their own models or not 
*make functions on the model to do the math of monthly income/ yearly income/ etc 
* 




REACT:
has grid system for the profiles/ can be dragged and dropped to relocate on page and it'll save/ you can change the view appearance where it can either show the profiles to show you whats inside them individually
or you can look at the view to see the total of income and the total of expenses.
the objectives page should look like a list with a bar graph showing amount completed? 
goals should / can relate to the accounts that are set up on the financial side; 
or show a total of all goals listed 

the react pages should have a pop up of text onHover that shows/explains what each thing is- it should show you if  you hover over the work fluctuating - that means anything that needs to be cacluated on a as added basis- could be gig jobs, independent contractors, self employeed, buisness owners etc. 
