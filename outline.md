# Anomaly Detection Project
## Robert Murphy and Tyler Applegate, Florence Cohort, 2021_07_22

#### Email:
Hello,

I have some questions for you that I need to be answered before the board meeting Thursday afternoon. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.

#### Questions to Answer:
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?

#### Project Specs:
- [] To get 100 on this project you only need to answer 5 out of the 7 questions (along with the other deliverables listed below i.e. slide, your notebook, etc).
- [] Due Thursday 07/22 no later than 12:30 p.m.; send your email to datascience@codeup.com (Only one team member can do this on behalf of whole team).
- [] Submit a link to a final notebook on GitHub that asks and answers questions - document the work you do to justify findings
- [] Compose an email with the answers to the questions/your findings, and in the email, include the link to your notebook in GitHub and attach your slide.
- [] You will not present this, so be sure that the details you need your leader to convey/understand are clearly communicated in the email.
- [] Your slide should be like an executive summary and be in form to present.
- [] Continue to use best practices of acquire.py, prepare.py, etc.
- [] Since there is no modeling to be done for this project, there is no need to split the data into train/validate/test
- [] The cohort schedule is in the SQL database, and alumni.codeup.com has info as well.
- []  Teamwork with Git handout is posted in the google classroom

#### Additional Resources:

- [GitHub Teamwork](https://drive.google.com/file/d/1Bd44VFDipdAsxvrFc5j8YNSMYyHJ8ju-/view?usp=sharing)

### Project Planning
- General Planning
- Data Acquisition
- Data Preparation
- Data Exploration
- Modeling
- Conclusion & Next Steps
- Presentation
#### General Planning: Both
- [] Environment setup
- [] Project Goals / Deliverables
- [] Division of Labor
- [] MVP vs 'with more time'
- [] Timeline
- [] Function Modules
- [] Final Notebook
- [] Google Slide
#### Data Acquisition: Tyler
- [x] Write a SQL query to join the cohorts and logs tables in the curriculum_logs dataset located in the Codeup databse.
- [x] Write a functon that will call this SQL query, return a pandas DataFrame, and save it locally as a csv
- [x] Write a second function that will look first for the locally stored csv file to optimize performance, and only connect to the Codeup database if the file is not available locally.
- [] Store all functions in acquire.py so the results are resproducible. Make sure all functions have full doc-strings, and comments.
- [] Add the data acquisition with full markdown/comments into the final_report notebook
- [] Final Notebook:
    - [] Key Findings and Takeaways
    - [] Data Preparation First Iteration To-Do
#### Data Preparation: 
- [] Complete all steps in the Data Preparation First Iteration To-Do list.
    - [] Concatenate 'date' and 'time', convert to datetime, and reset as index.
    - [] Convert all time-bound variables to datetime format
    - [] Drop unnecessary columns
    - [] Drop null values
- [] Store all functions in prepare.py so the results are resproducible. Make sure all functions have full doc-strings, and comments.
- [] Add the data preparation with full markdown/comments into the final_report notebook
- [] Final Notebook:
    - [] Key Findings and Takeaways
    - [] Data Exploration First Iteration To-Do
#### Data Exploration:
- [] Complete all steps in the Data Exploration First Iteration To-Do List:
    - []
- [] Store all functions in explore.py so the results are resproducible. Make sure all functions have full doc-strings, and comments.
- [] Add the data exploration with full markdown/comments into the final_report notebook
- [] Final Notebook:
    - [] Key Findings and Takeaways
    - [] Modeling First Iteration To-Do
#### Modeling:
- Complete all steps in the Modeling First Iteration To-Do List:
    - []
    - []
- [] Store all functions in model.py so the results are resproducible. Make sure all functions have full doc-strings, and comments.
- [] Add the modeling with full markdown/comments into the final_report notebook
- [] Final Notebook:
    - [] Key Findings and Takeaways
    - [] Second Iteration To-Do
#### Conclusions / Next Steps:
- [] Write a detailed conclusion complete with next steps, and add to Final Report Notebook.
- [] Make sure to include a detailed 'with more time' section
#### Final Report Notebook:
- [] Project Planning
- [] Project Goals
- [] Project Deliverables
- [] Data Acquisition
- [] Data Preparation
- [] Data Exploration
- [] Modeling
- [] Conclusions / Next Steps
#### Google Slide:
- [] Create 1 slide that shows the 'one big takeaway' from our research
- [] Refer to the email to ensure all questions are answered
#### Deliverables:
- [] Turn in link to Final Report Notebook
- [] Email Google Slide
- [] 



