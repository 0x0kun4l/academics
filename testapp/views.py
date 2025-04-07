from django.shortcuts import render

def home_page_view(request):
    return render(request, 'home.html')

def faculty_page_view(request):
    return render(request, 'faculty.html')

def student_page_view(request):
    return render(request, 'student.html')

def event_page_view(request):
    return render(request, 'event.html')