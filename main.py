#!/usr/bin/env python3

from fpdf import FPDF
import random
import sys

def sign(n):
    if(n >= 0):
        return '+'
    else:
        return '-'

def create_equation(param='x'):
    """
    returns an equation with the answer 

    the equestion should be in the form of 
    ax + b = c
    such that the solution is a whole number (between -10 and 10)
    
    start with the solution n 
    x = n
    multiply by random number a
    ax = na
    add random number b
    ax + b = na + b
    """
    n = random.randint(-10,10)
    a = random.choice([i for i in range(-10,11,1) if i != 0]) # integers between -10 and 10 without 0 
    b = random.randint(-50,50)
    c = n*a + b
    equation_string = '{}{} {} {} = {}'.format(a,param,sign(b), abs(b),c)
    return (equation_string, n, param)


def create_equation_list(n):
    """
    returns a list of equation
    """
    questions = []
    for _ in range(n):
        questions.append(create_equation(random.choice('xkmnab')))
    return questions

questions = create_equation_list(int(sys.argv[1]))

pdf = FPDF()
pdf.set_font('Arial', '', 30)
pdf.add_page()
pdf.cell(50)
# printing the title
pdf.cell(90, 10, 'Math Worksheet', 0, 0, 'U')
pdf.ln(30)
pdf.set_font_size(20)
for index, question in enumerate(questions):
    # printing the question
    pdf.cell(95, 10, '{}. {}'.format(index+1, question[0]))
    pdf.ln(100)
    # printing the box
    pdf.cell(50, 12, '{} =   '.format(question[2]), 1)
    pdf.ln(20)
    # adding a new page every 2 questions
    if(index % 2 == 1):
        pdf.add_page()

#printing the answer key title
pdf.cell(60)
pdf.cell(90, 10, 'Answer Key', 0, 0, 'U')
pdf.ln(30)
pdf.set_font_size(20)
# printing the answer for every question
for index, question in enumerate(questions):
    # printing the answer cell
    pdf.cell(39, 10, '{}. {} = {}'.format(index+1, question[2], question[1]), 1)
    # dropping a line every 6 answers
    if(index % 5 == 4):
       pdf.ln(h = '')
pdf.output('result.pdf')