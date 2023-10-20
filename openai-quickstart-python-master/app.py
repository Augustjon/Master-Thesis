import os
import json
import openai
import time
import random
import ast

openai.api_key_path ="apikey.txt" 

str1 = "Case1"
str2 = "Case2"
str3 = "Case3"



def test():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages=[
            {"role": "system", "content": """You are an assistant that focus on creating multiple choice questions about 
            programing. The answer should be formated as a JSON with the following structure. Do not deviate from this!
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
                                            """},
            {"role": "user", "content": "create 10 questions about for loops"}
        ],
    )
    return response.choices[0].message.content
    

def create_questions_Case1():
    f = open("Skillmap.JSON")
    map = json.load(f)
    mapString = json.dumps(map)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages= [
            {"role": "system", "content": """ You are an assistant that focus on creating a set of multiple choice questions about a topic in the 
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
             """},
            {"role": "user", "content": "Here is a skillmap of conditional statements in Golang " + mapString},
            {"role": "user", "content": "Create 10 questions about conditional statements in Golang"},
        ]
    )
    return response.choices[0].message.content


def create_questions_Case2():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages= [
             {"role": "system", "content": """ You are an assistant that focus on creating a set of multiple choice questions about a topic in the 
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
             """},
             {"role": "user", "content": """ Can you create 10 multiple-choice questions about conditional statements in Golang.
              The questions should have a sense of progression of complexity acording to complexity levels. They should also have a sensible order of the questions. The different complexity levels are
              level 1-recall: theses questions go into basic fact checking. the questions could for example be about syntax for conditional statements.
              level 2-Apply and understand: these questions should require knowledge from multiple sources. 
              level 3-Analyze: These questions should be more complex than level 1 and 2 and require more indept knowledge about something. Basic recall cant answer these types of questions. Could inlcude code reading and understanding code execution.
              """}
        ]
    )
    return response.choices[0].message.content


def create_questions_Case3():
    f = open("Skillmap.JSON")
    f2 = open("Prereq.JSON")
    preMap = json.load(f2)
    map = json.load(f)
    mapString = json.dumps(map)
    mapPreString = json.dumps(preMap)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages=[
            {"role": "system", "content": """ You are an assistant that focus on creating a set of multiple choice questions about a topic in the 
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
             """},
            {"role": "user", "content":  """ Can you create 10 multiple-choice questions about conditional statements in Golang.
              The questions should have a sense of progression of complexity acording to complexity levels. There is an expected amount of Prerequisites already known that will be shown in the next prompt.
              The prompt after that gives a sugesstion of a map of topics that should be covered in the questions. Be creative when creating the questions, dont just take one of the skills from the skillmap and turn them into questions. 
              The different complexity levels are
              level 1-recall: theses questions go into basic fact checking. the questions could for example be about syntax for conditional statements.
              level 2-Apply and understand: these questions should require knowledge from multiple sources. 
              level 3-Analyze: These questions should be more complex than level 1 and 2 and require more indept knowledge about something. Basic recall cant answer these types of questions. Could inlcude code reading and understanding code execution.
              """},
            {"role": "user", "content": "This is the map of Prerequisites that a person has \n" + mapPreString},
            {"role": "user", "content": "This is the map of topics that the questions should follow \n" + mapString}
        ]
    )
    return response.choices[0].message.content

def parse_response(response, filename, case,x):
    f = open(filename + ".txt", "r+")
    f2 = open(filename + "raw.JSON", "r+")
    f3 = open("keys.txt","a")
    print(response)
    print(type(response))
    response = ast.literal_eval(response)
    print(type(response))
    try:
        file_data = json.load(f2)
    except ValueError as err:
        print("invalid JSON error: " + str(err))
    key = random.randint(0,1000)
    response["key"] = str(key)
    file_data[str(x)] = response
    f2.seek(0)
    json.dump(file_data, f2, indent=4)
    f.write(str(key))
    f.write("\n")
    f3.write("key: " + str(key) + " case: " + case)
    f3.write("\n")
    for question in response["questions"]:
        f.write(question["question"])
        f.write("\n")
    f.close()
    f2.close()
    f3.close()
        
def run_case1(filename,x):
    #for i in range(1):
    #print("run " + str(i))
    questions = test()
    #print(questions)
    parse_response(questions, filename, str1,x)
    
def run_case2(filename,x):
    #for i in range(1):
    #print("run " + str(i))
    questions = test()
    #print(questions)
    parse_response(questions, filename, str2, x)
    
def run_case3(filename, x):
    #for i in range(1):
    #print("run " + str(i))
    questions = test()
    #print(questions)
    parse_response(questions, filename, str3, x)        

def main():
    start_time = time.time
    for i in range(5):
        print("run: " + str(i))
        run_case1("case1",i)
        run_case2("case2",i)
        run_case3("case3",i)
    
    #run_case1("testtest")
    #run_case3("test")
    print("Duration {}".format(time.time() - start_time))
    
    
    
if __name__ == '__main__':
    main()



