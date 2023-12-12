pre appended instructions before each case.

""" You are an assistant that focus on creating a set of multiple choice questions about a topic in the
             programming language Golang. The questions generated should be formated as a single JSON with the following structure. Do not deviate from this! 
             Structure:
             {
                 "questions": [
                     {
                        "question": "",
                        "options": {
                            "A": "",
                            "B": "",
                            "C": "",
                            "D": "",
                        }
                        "Correct_answer": ""
                     },
                     {
                        "question": "",
                        "options": {
                            "A": "",
                            "B": "",
                            "C": "",
                            "D": "",
                        }
                        "Correct_answer": ""
                     },
                 ]
             }
             """
Case 1:
"Create 10 questions about conditional statements in Golang"   

Case 2:
""" Can you create 10 multiple-choice questions about conditional statements in Golang.
              The questions should have a sense of progression of complexity acording to complexity levels. They should also have a sensible order of the questions. The different complexity levels are
              level 1-recall: theses questions go into basic fact checking. the questions could for example be about syntax for conditional statements.
              level 2-Apply and understand: these questions should require knowledge from multiple sources.
              level 3-Analyze: These questions should be more complex than level 1 and 2 and require more indept knowledge about something. Basic recall cant answer these types of questions. Could inlcude code reading and understanding code execution.
              """          

Case 3:
""" Can you create 10 multiple-choice questions about conditional statements in Golang.
              The questions should have a sense of progression of complexity acording to complexity levels. There is an expected amount of Prerequisites already known that will be shown in the next prompt.
              The prompt after that gives a sugesstion of a map of topics that should be covered in the questions. Be creative when creating the questions, dont just take one of the skills from the skillmap and turn them into questions.
              The different complexity levels are
              level 1-recall: theses questions go into basic fact checking. the questions could for example be about syntax for conditional statements.
              level 2-Apply and understand: these questions should require knowledge from multiple sources.
              level 3-Analyze: These questions should be more complex than level 1 and 2 and require more indept knowledge about something. Basic recall cant answer these types of questions. Could inlcude code reading and understanding code execution.
              """
prompt after:
"This is the map of Prerequisites that a person has \n" + mapPreString
last prompt:
"This is the map of topics that the questions should follow \n" + mapString
