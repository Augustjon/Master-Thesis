import os
import json
import openai
import time

openai.api_key_path ="apikey.txt" 


def test():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages=[
            {"role": "system", "content": """You are an assistant that focus on creating multiple choice questions about topics in 
                                            the programing language Golang. The answer should be formated as a JSON with the following structure. Do not deviate from this!
                                            Structure:
                                            { 
                                                "question": "", 
                                                "optionA": "", 
                                                "optionB": "",
                                                "optionC": "", 
                                                "optionD": "",
                                                "correctOption": "",
                                                "explanation": "",
                                            }
                                            """},
            {"role": "user", "content": "create 5 questions about conditionals in Golang"}
        ],
    )
    return response.choices[0].message.content
    

def create_questions_Case1():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages= [
            {"role": "system", "content": """ You are an assistant that focus on creating a set of multiple choice questions about a topic in the 
             programming language Golang. The questions genereated should be formated as a single JSON with the following structure. Do not deviate from this! 
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
            {"role": "user", "content": "create 10 questions about conditional statements in Golang"},
        ]
    )
    return response.choices[0].message.content


def create_questions_Case2():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages= [
            {}
        ]
    )
    return response.choices[0].message.content


def create_questions_Case3():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=2048,
        messages= [
            {}
        ]
    )
    return response.choices[0].message.content

def parse_response(response, filename):
    f = open(filename + ".txt", "w")
    f2 = open(filename + "raw.txt", "w")
    map = json.loads(response)
    
    for question in map["questions"]:
        f.write(question["question"])
        f.write("\n")
        f2.write(str(question))
        f2.write("\n")
    f.close()
    f2.close()
        
    


def main():
    start_time = time.time
    for i in range(3):
        print("run " + str(i))
        questions = create_questions_Case1()
        print(questions)
        parse_response(questions, "test2" + str(i))
    print("Duration {}".format(time.time() - start_time))
    
    
    
if __name__ == '__main__':
    main()