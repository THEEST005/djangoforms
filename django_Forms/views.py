from django.shortcuts import render

from .form import UserReg
from .form import PeopleReg
from .form import StudentReg


def Reg(request):
    submit_button = request.POST.get('stacey')
    name = ''
    email = ''
    password = ''

    rForm = UserReg(request.POST or None)
    if rForm.is_valid():
        name = rForm.cleaned_data.get("name")
        email = rForm.cleaned_data.get("email")
        password = rForm.cleaned_data.get("password")

    context = {'rForm': rForm, 'name': name, 'email': email, 'submit_button': submit_button}
    return render(request, 'register.html', context)


def reg_people(request):
    submit_people_button = request.POST.get("people_btn")
    name = ''
    age = ''
    phone = ''
    city = ''

    people_form = PeopleReg(request.POST or None)
    if people_form.is_valid():
        name = people_form.cleaned_data.get("name")
        age = people_form.cleaned_data.get("age")
        phone = people_form.cleaned_data.get("phone")
        city = people_form.cleaned_data.get("city")

    context = {'people_form': people_form, 'name': name, 'age': age, 'phone': phone, 'city': city

               }
    return render(request, 'people.html', context)


def reg_student(request):
    submit_student_button = request.POST.get("student_btn")
    name = ''
    gender = ''
    school = ''
    parent = ''
    phonenumber = ''

    student_form = StudentReg(request.POST or None)
    if student_form.is_valid():
        name = student_form.cleaned_data.get("name")
        gender = student_form.cleaned_data.get("gender")
        school = student_form.cleaned_data.get("school")
        parent = student_form.cleaned_data.get("parent")
        phonenumber = student_form.cleaned_data.get("phone number")

    context = {'student_form': student_form, 'name': name, 'gender': gender, 'school': school, 'parent': parent,
               'phonenumber': phonenumber, 'submit_student_button': submit_student_button

               }
    return render(request, 'student.html', context)
