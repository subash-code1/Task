from django.shortcuts import render, redirect
from .models import Department, Doctor, Token
from io import BytesIO
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph,Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib import colors
from django.http import HttpResponse

def select_department(request):
    departments = Department.objects.all()
    print("-----",departments)
    return render(request, 'select_department.html', {'departments': departments})



def select_doctor(request):
    
    department_id = request.POST.get('department')
    department = Department.objects.get(id=department_id)
    doctors = Doctor.objects.filter(department=department)
    return render(request, 'select_doctor.html', {'doctors': doctors})

def confirm_token(request):
    
    doctor_id = request.POST.get('doctor')
    doctor = Doctor.objects.get(id=doctor_id)
    department = doctor.department
    current_token = Token.objects.filter(department=department).last()
    next_token_number = current_token.number + 1 if current_token else 1
    approximate_waiting_time = (Token.objects.filter(department=department).count() * 10)
    return render(request, 'confirm_token.html', {'doctor': doctor, 'next_token_number': next_token_number, 'current_token': current_token, 'approximate_waiting_time': approximate_waiting_time})


def generate_token(request, doctor_id):

    doctor = Doctor.objects.get(id=doctor_id)
    department = doctor.department
    current_token = Token.objects.filter(department=department).last()
    next_token_number = current_token.number + 1 if current_token else 1
    approximate_waiting_time = (Token.objects.filter(department=department).count() * 10)
    
    doctor_short_name = ''
    if " " in doctor.name:
        first_initial =  doctor.name.split()[0][0]
        second_initial =  doctor.name.split()[1][0]
        doctor_short_name = first_initial + second_initial
    else:
        doctor_short_name = doctor.name[:2]
    token_abbreviation = department.abbreviation + '-' + doctor_short_name.upper() + '-' + str(next_token_number)
    
    
    if current_token:
        token = Token.objects.create(number=next_token_number, department=department, doctor=doctor, current_token=current_token.number, approximate_waiting_time = approximate_waiting_time, doctor_name = doctor.name, token_name = token_abbreviation)
    else:
        token = Token.objects.create(number=next_token_number, department=department, doctor=doctor, current_token=0, approximate_waiting_time = 0, doctor_name = doctor.name, token_name = token_abbreviation)

    return render(request, 'token_generated.html', {'token_abbreviation': token_abbreviation, "doctor" : doctor, "token": token})


def call_next_patient(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return redirect('token_called')

def reset_tokens(request):
    Token.objects.all().delete()
    return render(request, "token_reset.html")



def download_pdf(request, token_id):

    token_number = Token.objects.get(id=token_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}-Token.pdf"'.format(token_number.token_name)

    buffer = BytesIO()
    p = SimpleDocTemplate(buffer, pagesize=letter)

    styles = getSampleStyleSheet()


    heading = Paragraph("Token Details", style=styles["Heading1"])

    data= [['Token Number', 'Doctor Name', 'Department', 'Date and Time'],
           [token_number.number, token_number.doctor.name, token_number.doctor.department.name, token_number.created_at]]
    t=Table(data)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.gray),
                           ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                           ('ALIGN',(0,0),(-1,-1),'CENTER'),
                           ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0,0), (-1,0), 12),
                           ('BACKGROUND',(0,-1),(-1,-1),colors.beige),
                           ('GRID',(0,0),(-1,-1),1,colors.black)]))
    p.build([heading,t])
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
