# AutoSurveyDelete
An automation script designed to quickly remove employees from a corporate database if marked as "Incomplete".

## The Scenario
* Excel file with over 600 employees
* Company database with a search system that does not support bulk querying
* There is an unknown amount of employees that are marked in the company database as "Incomplete"

## The Task
Manually look through each entry, grab the employee's first and last name and search them within the corporate system.
If they show up, check if they are marked "Incomplete". If so, remove them by clicking the red X button next to their name.
Within the Excel file, mark employees that have either been removed or were never in the system using the color orange.

## The Solution
Because a quick solution was needed as this assignment was a 24-hour deadline, lightweight automation libraries seemed to have promise.
1. Pyautogui - A python automation library, easy to install and operate. For this one-time scenario the use of pixel coordinates was acceptable.
1. JavaScript - Once the script reached the webpage, this is used to verify the employee was supposed to be removed.
1. Batch file - This would be used to create a loop in order to execute the script over all employee rows.
1. Inspect Console Window - This is used to manually write JavaScript queries.

## Animation of completed script running
###### NOTE: Each frame has been blurred to redact private/confidential information from both employees and their employer.
![Animated gif of automation](https://github.com/Sakari-Woods/AutoSurveyDelete/blob/main/automation.gif)

## The Automation Process
1. Click on the Last name of the employee and copy it via Ctrl+C.
1. Alt-Tab to the company search window.
1. Press the page-up key 5 times (this is to reset the page back to the top if the previous employee search forced scrolling downward).
1. Click on the search bar.
1. Press backspace and delete 10 times to clear the box (delete is also pressed as the full-select will omit names containing dashes, which is problematic).
1. Ctrl+V the last name into the search.
1. Press enter to search.
1. Alt-Tab back to the Excel file.
1. Navigate one column over and Ctrl+C the employee's first name.
1. Alt-Tab back to the company search window.
1. Ctrl+F to bring up the text-search for the browser.
1. Ctrl+V the first name into the text-search.
1. Compare the image of "0/0" results found and check if it exists on the page (This is using pyautogui's openCV pattern recognition).
In the event the sub-image of "0/0" is found, this means the first name was not located, and therefore the employee does not exist.


If the image was not found, this means there was a result where both first and last names exist within the search results.
1. Click on the right-side of the page (this is to set focus to the console window opened prior to script execution).
1. Type JavaScript in to grab all search result rows and store them in "var target".
Write a while loop that repeatedly removes search results from the target list until one is found that matches the first name.
1. Ctrl+V the first name in the middle of the search query loop.
1. Continue writing JavaScript query, and compare the last name to what is already entered into the company search bar.
1. Press enter twice (This is pressed twice mostly as a sanity check).
1. Alt-Tab back to the Excel file.
1. Set the employee name to be highlighted in orange, and set focus to the next employee's last name.

## Results
While writing the program ended up taking about 2 hours, once running, the laptop would continuously run through each and every result, allowing the user to focus on more constructive tasks.
An audio beep was played at different frequencies when an employee was either removed or never existed. This helped reduce the tendency to constantly check whether the script was still running,
or if was just clicking around like crazy (as pixel-coordinate-using scripts can easily turn into).

**All entries were correctly processed within 9 hours, freeing the user to focus on other tasks.**

## What Was Learned
* PyAutoGui is unable to scrape text data, and can only search for images on the screen.
* Using time.sleep with PyAutoGui proves to be extremely problematic, as each loop the program executes the script becomes more unstable. This could be due to constantly creating new processes that are forced to wait for execution. 
This issue was solved by placing the looping mechanic within a batch file that invokes the script, and by using PyAutoGui's built-in delay that affects every automation call.
* It would be useful to access files on a computer with JavaScript during an automation process, maybe through a mini-node-automation server prebuilt for mundane office tasks.
